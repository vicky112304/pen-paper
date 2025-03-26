from flask import Flask, render_template, request, redirect, url_for, flash, session, g,jsonify
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import time
import math
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from Levenshtein import ratio
import torch

app = Flask(__name__)
# nltk.download("wordnet")
# nltk.download("stopwords")
# nltk.download("punkt")

# nltk.download("punkt_tab")
mnli_tokenizer = AutoTokenizer.from_pretrained("roberta-large-mnli")
mnli_model = AutoModelForSequenceClassification.from_pretrained("roberta-large-mnli")
sbert_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
mnli_model.to(device)
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
def check_contradiction(sentence1, sentence2):
    inputs = mnli_tokenizer.encode_plus(
        sentence1, sentence2, return_tensors="pt", truncation=True, padding="longest"
    ).to(device)
    outputs = mnli_model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1).squeeze().tolist()
    contradiction_prob = probs[0] * 100
    return round(contradiction_prob, 1)

def preprocess_text(sentence):
    words = word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]

def word_match_percentage(sentence2, sentence1):
    words1 = preprocess_text(sentence1)
    words2 = preprocess_text(sentence2)
    matched_words = set(words1) & set(words2)
    match_percentage = (len(matched_words) / len(words1)) * 100 if words1 else 0
    return round(match_percentage, 2), matched_words

def sentence_order_similarity(sentence1, sentence2):
    return round(ratio(" ".join(preprocess_text(sentence1)), " ".join(preprocess_text(sentence2))) * 100, 2)

def semantic_similarity(sentence1, sentence2):
    embeddings = sbert_model.encode([sentence1, sentence2])
    return round(util.pytorch_cos_sim(embeddings[0], embeddings[1]).item() * 100, 2)

def calculate_marks(sentence1, sentence2, total_marks):
    contradiction_score = check_contradiction(sentence1, sentence2)
    if contradiction_score >= 60:
        return 0
    word_match, _ = word_match_percentage(sentence1, sentence2)
    order_similarity = sentence_order_similarity(sentence1, sentence2)
    semantic_score = semantic_similarity(sentence1, sentence2)
    print(semantic_score)
    final_score = max(0, (0.98 * word_match) + (0.01 * order_similarity) + (0.01 * semantic_score))
    obtained_marks = min(total_marks, math.floor(final_score / 100 * total_marks))
    return obtained_marks

app.secret_key = 'vignesh'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'desexam'
mysql = MySQL(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'penpaperonline25@gmail.com'
app.config['MAIL_PASSWORD'] = 'wwohfxkbcnnjblez'
mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/register', methods=['GET', 'POST'])
def register():
    connection = mysql.connection  
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM departments")
    departments = cursor.fetchall()
    cursor.execute("SELECT id, name FROM batches")
    batches = cursor.fetchall()
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        department_id = request.form['department']
        batch_id = request.form['batch']
        if not full_name or not email or not password or not department_id or not batch_id:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))
        cursor.execute("SELECT id FROM register WHERE mail_id = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Email already exists. Please try logging in.', 'danger')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        try:
            cursor.execute(
                "INSERT INTO register (mail_id, password, role) VALUES (%s, %s, %s)",
                (email, hashed_password, "STUDENT")
            )
            connection.commit()
            cursor.execute("SELECT id FROM register WHERE mail_id = %s", (email,))
            new_user = cursor.fetchone()
            
            user_id = new_user[0]
            print("user_id",user_id)
            cursor.execute(
                "INSERT INTO students (user_id, name, email, department_id, batch_id) VALUES (%s, %s, %s, %s, %s)",
                (user_id, full_name, email, department_id, batch_id)
            )
            connection.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            connection.rollback()
            print(e)
            flash('Error during registration: ' + str(e), 'danger')
            return redirect(url_for('register'))
    cursor.close()
    return render_template('register.html', departments=departments, batches=batches)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        connection = mysql.connection 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM register WHERE mail_id = %s", (email,))
        user = cursor.fetchone()
        if user and check_password_hash(user[2], password):  
            session['user_id'] = user[0]  
            session['role'] = user[3]    
            if user[3] == 'ADMIN':
                return redirect(url_for('admin_dashboard'))
            elif user[3] == 'TEACHER':
                return redirect(url_for('teacher_dashboard'))
            elif user[3] == 'STUDENT':
                return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

# @app.route('/view_results/<int:exam_id>')
# def view_results(exam_id):
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
    
#     user_id = session['user_id']
#     print("User ID:", user_id, "Exam ID:", exam_id)

#     cur = mysql.connection.cursor()

    
#     query = """
#         SELECT s.id, s.name, COALESCE(SUM(a.mark), 0) AS obtained_marks, 
#                (SELECT SUM(q.marks) FROM questions q WHERE q.id IN (SELECT question_id FROM answers WHERE exam_id = %s)) 
#                AS total_marks
#         FROM students s
#         LEFT JOIN answers a ON s.id = a.student_id AND a.exam_id = %s
#         GROUP BY s.id, s.name
#     """
#     cur.execute(query, (exam_id, exam_id))
#     results = cur.fetchall()

#     return render_template('view_results.html', results=results, exam_id=exam_id)

@app.route('/view_result/<int:exam_id>')
def view_result(exam_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    print("user id",user_id," exam id ",exam_id)
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM students WHERE user_id = %s", (user_id,))
    student = cur.fetchone()
    if not student:
        return "Student not found", 404
    student_id = student[0]
    print("student id",student_id)
    query = """
        SELECT q.question, q.answer AS correct_answer, q.marks, a.answer_given, a.mark 
        FROM answers a
        JOIN questions q ON a.question_id = q.id
        WHERE a.exam_id = %s AND a.student_id = %s
    """
    cur.execute(query, (exam_id, student_id))
    results = cur.fetchall()
    total_marks_obtained = sum(row[4] for row in results)  
    total_possible_marks = sum(row[2] for row in results) 
    return render_template('view_result.html', results=results, exam_id=exam_id,
                           total_marks_obtained=total_marks_obtained,
                           total_possible_marks=total_possible_marks)
@app.route('/view_results/<int:exam_id>')
def view_results(exam_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    print("User ID:", user_id, "Exam ID:", exam_id)
    cur = mysql.connection.cursor()
    query = """
        SELECT s.id, s.name, COALESCE(SUM(a.mark), 0) AS obtained_marks, 
               (SELECT SUM(q.marks) FROM questions q WHERE q.id IN (SELECT question_id FROM answers WHERE exam_id = %s)) 
               AS total_marks
        FROM students s
         JOIN answers a ON s.id = a.student_id AND a.exam_id = %s
        GROUP BY s.id, s.name
    """
    cur.execute(query, (exam_id, exam_id))
    results = cur.fetchall()
    return render_template('view_results.html', results=results, exam_id=exam_id)


def fetch_data(query):
    connection = mysql.connection 
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

@app.route('/get_students')
def get_students():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  students.id, students.name, students.email, departments.name, batches.name FROM students JOIN departments ON departments.id = students.department_id JOIN batches ON batches.id = students.batch_id;")
    students = cursor.fetchall()
    cursor.close()
    return jsonify([{'id': s[0], 'name': s[1], 'email': s[2], 'department': s[3],'batch':s[4]} for s in students])
@app.route('/get_student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT id, name, email, department_id, batch_id
        FROM students  WHERE students.id = %s;
    """, (student_id,))
    student = cursor.fetchone()
    cursor.close()

    if student:
        return jsonify({
            'id': student[0],
            'name': student[1],
            'email': student[2],
            'department': student[3],
            'batch': student[4]
        })
    else:
        return jsonify({'error': 'Student not found'}), 404 

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (name, email, batch_id,department_id) VALUES (%s, %s, %s,%s)", 
                   (data['name'], data['email'], data['batch'],data['department']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Student added successfully!'})
def insert_data(query, params=None, fetch=False):
    connection = mysql.connection
    cursor = connection.cursor()
    try:
        cursor.execute(query, params or ())
        connection.commit()
        
        if fetch: 
            return cursor.lastrowid  
        
        return True  
    except Exception as e:
        connection.rollback()
        flash(f"Error: {str(e)}", "danger")
        return False
    finally:
        cursor.close()
@app.route('/add_exam', methods=['POST'])
def add_exam():
    if 'user_id' not in session or session.get('role').lower() != 'teacher':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('login'))

    try:
        user_id=session.get("user_id")
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id FROM teachers WHERE user_id = %s", (user_id,))
        teacher = cursor.fetchone()
        
        subject = request.form.get("subject")
        exam_date = request.form.get("date")
        exam_time = request.form.get("time")
        time_limit = request.form.get("time_limit")
        teacher_id = 1
        department_id = request.form.get("department_id")
        batch_id = request.form.get("batch_id")
        teacher_id=teacher[0]
        print(f"Received Exam Data: {subject}, {exam_date}, {exam_time}, {time_limit}, {teacher_id}, {department_id}, {batch_id}")

        if not (subject and exam_date and exam_time and time_limit and department_id and batch_id):
            flash('All fields are required!', 'danger')
            return redirect(url_for('teacher_dashboard'))

        
        insert_query = """
            INSERT INTO exams (name, date, time, time_limit, teacher_id, department_id, batch_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        exam_id = insert_data(insert_query, (subject, exam_date, exam_time, time_limit, teacher_id, department_id, batch_id), fetch=True)

        if not exam_id:  
            flash('Failed to create exam!', 'danger')
            return redirect(url_for('teacher_dashboard'))

        print(f"Exam Inserted with ID: {exam_id}")

        # Extract question details
        questions = request.form.getlist("question[]")  # Updated to match form names
        answers = request.form.getlist("answer[]") 
        marks = request.form.getlist("marks[]")  

        print(f"Questions Received: {questions}, {answers}, {marks}")

        if not questions or not answers or not marks or len(questions) != len(answers) or len(answers) != len(marks):
            flash("Invalid question data!", "danger")
            return redirect(url_for('teacher_dashboard'))

        try:
            for question, answer, mark in zip(questions, answers, marks):
                insert_question_query = """
                    INSERT INTO questions (question, answer, marks, exam_id)
                    VALUES (%s, %s, %s, %s);
                """
                result = insert_data(insert_question_query, (question, answer, mark, exam_id))
                print(f"Question Inserted: {question}, Status: {result}")
        except Exception as e:
            print(str(e))
        print("last")
        flash('Exam created successfully with questions!', 'success')

    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        print(f"Exception Occurred: {str(e)}")

    return redirect(url_for('teacher_dashboard'))

@app.route('/update_student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    department = data.get('department')
    batch = data.get('batch')
    if not name or not email or not department or not batch:
        return jsonify({'error': 'Missing required fields'}), 400
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("""
            UPDATE students
            SET name = %s, email = %s, 
                department_id = %s, 
                batch_id = %s
            WHERE id = %s;
        """, (name, email, department, batch, student_id))
        mysql.connection.commit()
        return jsonify({'message': 'Student updated successfully'}), 200
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
@app.route('/update_teacher/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    department_id = data.get('department')
    

    

    cursor = mysql.connection.cursor()
    try:
        cursor.execute("""
            UPDATE teachers
            SET name = %s, email = %s, 
                department_id = %s
            WHERE id = %s;
        """, (name, email, department_id,  teacher_id))
        mysql.connection.commit()
        return jsonify({'message': 'Teacher updated successfully'}), 200
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/delete_student', methods=['POST'])
def delete_student():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (data['id'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Student deleted successfully!'})

# ===================== 🎓 TEACHERS ROUTES =====================

@app.route('/get_teachers')
def get_teachers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT teachers.id, teachers.name, teachers.email, departments.name AS department_name FROM teachers JOIN departments ON departments.id = teachers.department_id;")
    teachers = cursor.fetchall()
    cursor.close()
    return jsonify([{'id': t[0], 'name': t[1], 'email': t[2], 'department': t[3]} for t in teachers])
@app.route('/get_teacher/<int:id>', methods=['GET'])
def get_teacher(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT teachers.id, teachers.name, teachers.email, departments.id AS department_name FROM teachers JOIN departments ON departments.id = teachers.department_id WHERE teachers.id = %s;", (id,))
    teacher = cursor.fetchone()
    cursor.close()

    if teacher:
        return jsonify({'id': teacher[0], 'name': teacher[1], 'email': teacher[2], 'department': teacher[3]})
    else:
        return jsonify({'error': 'Teacher not found'}), 404


@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    connection = mysql.connection  
    cursor = connection.cursor()

    data = request.json  
    full_name = data.get('name')
    email = data.get('email')
    department_id = data.get('department')

    if not full_name or not email or not department_id:
        return jsonify({'message': 'All fields are required!'}), 400

    cursor.execute("SELECT id FROM register WHERE mail_id = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        cursor.close()
        return jsonify({'message': 'Email already exists!'}), 400

    hashed_password = generate_password_hash("1234")

    try:
        cursor.execute(
            "INSERT INTO register (mail_id, password, role) VALUES (%s, %s, %s)",
            (email, hashed_password, "TEACHER")
        )
        connection.commit()

        cursor.execute("SELECT id FROM register WHERE mail_id = %s", (email,))
        new_user = cursor.fetchone()
        user_id = new_user[0]

        cursor.execute(
            "INSERT INTO teachers (user_id, name, email, department_id) VALUES (%s, %s, %s, %s)",
            (user_id, full_name, email, department_id)
        )
        connection.commit()

        cursor.close()
        return jsonify({'message': 'Teacher added successfully!'}), 201

    except Exception as e:
        connection.rollback()
        cursor.close()
        return jsonify({'message': 'Error during teacher registration: ' + str(e)}), 500


@app.route('/delete_teacher', methods=['POST'])
def delete_teacher():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM teachers WHERE id = %s", (data['id'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Teacher deleted successfully!'})

# ===================== 🏢 DEPARTMENTS ROUTES =====================

@app.route('/get_departments')
def get_departments():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, name FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    return jsonify([{'id': d[0], 'name': d[1]} for d in departments])

@app.route('/add_department', methods=['POST'])
def add_department():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO departments (name) VALUES (%s)", (data['name'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Department added successfully!'})

@app.route('/delete_department', methods=['POST'])
def delete_department():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM departments WHERE id = %s", (data['id'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Department deleted successfully!'})

# ===================== 🔄 BATCHES ROUTES =====================

@app.route('/get_batches')
def get_batches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, name FROM batches")
    batches = cursor.fetchall()
    cursor.close()
    return jsonify([{'id': b[0], 'name': b[1]} for b in batches])

@app.route('/add_batch', methods=['POST'])
def add_batch():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO batches (name, department) VALUES (%s, %s)", 
                   (data['name'], data['department']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Batch added successfully!'})

@app.route('/delete_batch', methods=['POST'])
def delete_batch():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM batches WHERE id = %s", (data['id'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Batch deleted successfully!'})

# ===================== 🌐 RUN SERVER =====================
@app.route("/test/<int:test_id>")
def start_test(test_id):
    connection = mysql.connection 
    cursor = connection.cursor()
    cursor.execute("SELECT time_limit FROM EXAMS WHERE id= %s",(test_id,))
    time_limit=cursor.fetchall()
    cursor.execute("SELECT * FROM questions WHERE exam_id = %s", (test_id,))
    questions = cursor.fetchall()
    return render_template('test.html',questions=questions,time_limit=time_limit[0][0],exam_id=test_id)

# @app.route('/submit', methods=['POST'])
# def submit_test():
#     connection = mysql.connection 
#     cursor = connection.cursor()
#     cursor.execute("SELECT id, question,answer, marks FROM questions")
#     rows = cursor.fetchall()
#     correct_answers = {str(row[0]): row[2] for row in rows}
#     get_marks = {str(row[0]): row[3] for row in rows}
#     questions = {str(row[0]): row[1] for row in rows}
#     print(correct_answers)
#     user_answers = {}
#     for key, value in request.form.items():
#         if key.startswith('answers_'):
#             question_id = key.split('_')[1]
#             user_answers[question_id] = value.strip()
#     print(user_answers)
#     results = {}
#     student_id = 1  
#     exam_id=1
#     for question_id, user_answer in user_answers.items():
#         correct_answer = correct_answers.get(question_id)
#         if correct_answer:
#             embedding1 = model.encode([user_answer])
#             embedding2 = model.encode([correct_answer])
#             similarity = cosine_similarity(embedding1, embedding2)
#             similarity_percentage = min(100, math.ceil(similarity[0][0] * 100))
#             total_marks = get_marks.get(question_id)
#             obtained_marks = min(total_marks, math.ceil(similarity_percentage / 100 * total_marks))
#             results[question_id] = {
#                 "question": questions[question_id],
#                 "user_answer": user_answer,
#                 "correct_answer": correct_answer,
#                 "obtained_marks": obtained_marks,
#                 "total_marks": total_marks,
#             }
            
#             try:
#                 cursor.execute("""
#                     INSERT INTO answers (student_id, question_id, exam_id, answer_given, mark)
#                     VALUES (%s, %s, %s, %s, %s)
#                 """, (student_id, question_id, exam_id, user_answer, obtained_marks))
#                 connection.commit() 
#             except Exception as e:
#                 print(f"Error inserting data: {e}")
    
#     total_marks = sum(data['total_marks'] for data in results.values())
#     obtained_marks = sum(data['obtained_marks'] for data in results.values())
#     print(total_marks,obtained_marks)
#     return render_template("result.html", results=results,total_marks=total_marks, obtained_marks=obtained_marks)
def get_student_id():
    student_id_query = "SELECT id FROM students WHERE user_id = {}".format(session['user_id'])
    result = fetch_data(student_id_query)
    print(result)
    return result[0][0] if result else None

@app.route('/submit', methods=['POST'])
def submit_test():
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("SELECT id, question, answer, marks FROM questions")
    rows = cursor.fetchall()
    correct_answers = {str(row[0]): row[2] for row in rows}
    get_marks = {str(row[0]): row[3] for row in rows}
    questions = {str(row[0]): row[1] for row in rows}
    user_answers = {}
    for key, value in request.form.items():
        if key.startswith('answers_'):
            question_id = key.split('_')[1]
            user_answers[question_id] = value.strip()
    
    results = {}
    user_id=session["user_id"]
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM students WHERE user_id = %s", (user_id,))
    student = cursor.fetchone()
    student_id = student[0]
    exam_id = request.form.get("exam_id", 1)  
    for question_id, user_answer in user_answers.items():
        correct_answer = correct_answers.get(question_id)
        if correct_answer:
            obtained_marks = calculate_marks(user_answer, correct_answer, get_marks[question_id])
            results[question_id] = {
                "question": questions[question_id],
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "obtained_marks": obtained_marks,
                "total_marks": get_marks[question_id],
            }
            try:
                cursor.execute("""
                    INSERT INTO answers (student_id, question_id, exam_id, answer_given, mark)
                    VALUES (%s, %s, %s, %s, %s)
                """, (student_id, question_id, exam_id, user_answer, obtained_marks))
                connection.commit()
            except Exception as e:
                print(f"Error inserting data: {e}")
    
    total_marks = sum(data['total_marks'] for data in results.values())
    obtained_marks = sum(data['obtained_marks'] for data in results.values())
    return render_template("result.html", results=results, total_marks=total_marks, obtained_marks=obtained_marks)
@app.route("/features")
def features_page():
    return render_template("features.html")
@app.route('/admin')
def admin_dashboard():
     if 'user_id' not in session or session.get('role') != 'ADMIN':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('login'))
     past_exams_query = """
        SELECT e.id, e.name, e.date, e.time, e.time_limit, t.name AS teacher_name
        FROM exams e
        JOIN teachers t ON e.teacher_id = t.id
        WHERE e.date < CURDATE()
        ORDER BY e.date DESC;
    """ 
     past_exams = fetch_data(past_exams_query) 
     print(past_exams)
     return render_template("admin_dashboard.html", past_exams=past_exams)

@app.route('/teacher')
def teacher_dashboard():
    if 'user_id' not in session or session.get('role').lower() != 'teacher':
        flash('Unauthorized access!', 'danger') 
        return redirect(url_for('login'))
    teacher_info_query=f"""
            SELECT id, name, email, department_id 
            FROM teachers
            WHERE user_id ={session.get("user_id")};
    """
    connection = mysql.connection  
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM departments")
    departments = cursor.fetchall()
    cursor.execute("SELECT id, name FROM batches")
    batches = cursor.fetchall()
    teacher_info=fetch_data(teacher_info_query)[0]
    upcoming_exams_query = f"""
        SELECT id, date, time,time_limit,teacher_id 
        FROM exams 
        WHERE date >= CURDATE() AND teacher_id = {teacher_info[0]}
        ORDER BY date ASC;
    """ 
    past_exams_query = f"""
        SELECT id,name, date, time,time_limit
        FROM exams 
        WHERE date < CURDATE() AND teacher_id = {teacher_info[0]}
        ORDER BY date DESC;
    """
    upcoming_exams = fetch_data(upcoming_exams_query) 
    past_exams = fetch_data(past_exams_query)
    return render_template("teacher_dashboard.html",upcoming_exams=upcoming_exams, past_exams=past_exams,info=teacher_info,departments=departments,batches=batches)
@app.route('/student')
def student_dashboard():
    if 'user_id' not in session or session.get('role') != 'STUDENT':
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('login'))
    
    student_id = get_student_id()
    if not student_id:
        flash('Student ID not found!', 'danger')
        return redirect(url_for('login'))
    
    upcoming_exams_query = f"""
    SELECT id, name, date, time, time_limit
    FROM exams 
    WHERE date >= CURDATE() 
    AND id NOT IN (
        SELECT DISTINCT exam_id FROM answers WHERE student_id = {student_id}
    )
    ORDER BY date ASC;
    """

    
    past_exams_query = f"""
    SELECT DISTINCT e.id, e.name, e.date, e.time, e.time_limit
    FROM exams e
    LEFT JOIN answers a ON e.id = a.exam_id
    WHERE (e.date < CURDATE() OR a.exam_id IS NOT NULL)
    AND a.student_id = {student_id}
    ORDER BY e.date DESC;
"""

    upcoming_exams = fetch_data(upcoming_exams_query)
    past_exams = fetch_data(past_exams_query)

    return render_template("student_dashboard.html", upcoming_exams=upcoming_exams, past_exams=past_exams)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# @app.route('/departments')
# def departments():
#     connection = mysql.connection 
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM departments")
#     departments = cursor.fetchall()
#     print(departments)
#     return render_template('departments.html', departments=departments)

# @app.route('/department/add', methods=['POST'])
# def add_department():
#     name = request.form['name']
#     connection = mysql.connection 
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO departments (name) VALUES (%s)", (name,))
#     connection.commit()
#     return redirect(url_for('departments'))

# @app.route('/department/<int:id>/delete', methods=['POST'])
# def delete_department(id):
#     connection = mysql.connection 
#     cursor = connection.cursor()
#     cursor.execute("DELETE FROM departments WHERE id = %s", (id,))
#     return redirect(url_for('departments'))

# @app.route('/department/<int:department_id>/batches')
# def batches(department_id):
#     connection = mysql.connection 
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM batches WHERE department_id = %s", (department_id,))
#     batches = cursor.fetchall()
#     return render_template('batches.html', batches=batches, department_id=department_id)

# @app.route('/department/<int:id>/edit', methods=['GET', 'POST'])
# def edit_department(id):
#     connection = mysql.connection 
#     cursor = connection.cursor()
#     if request.method == 'POST':
#         name = request.form['name']
#         cursor.execute("UPDATE departments SET name = %s WHERE id = %s", (name, id))
#         connection.commit()
#         return redirect(url_for('departments'))
#     else:
#         cursor.execute("SELECT * FROM departments WHERE id = %s", (id,))
#         department = cursor.fetchone()
#         return render_template('edit_department.html', department=department)
@app.route('/forget_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        connection = mysql.connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM register WHERE mail_id = %s", (email,))
        user = cursor.fetchone()
        if user:
            token = s.dumps(email, salt='password-reset-salt')
            cursor.execute("DELETE FROM password_reset_tokens WHERE email = %s", (email,))
            cursor.execute("INSERT INTO password_reset_tokens (email, token) VALUES (%s, %s)", (email, token))
            connection.commit()
            reset_url = url_for('reset_password', token=token, _external=True)

            msg = Message('Password Reset Request - Pen and Paper Online',
                        sender='your_email@gmail.com',
                        recipients=[email])
            msg.html = f"""
            <html>
            <head>
                <style>
                    body {{
                        font-family: 'Poppins', sans-serif;
                        background-color: #f7f7f7;
                        color: #333;
                        text-align: center;
                        padding: 20px;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 10px;
                        padding: 30px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        animation: fadeIn 1s ease-in-out;
                    }}
                    h1 {{
                        color: #007bff;
                        font-size: 24px;
                    }}
                    p {{
                        margin: 15px 0;
                    }}
                    a {{
                        text-decoration: none;
                        color: #ffffff!important;
                        background-color: #007bff;
                        padding: 10px 20px;
                        border-radius: 5px;
                        font-weight: bold;
                        transition: background-color 0.3s ease;
                    }}
                    a:hover {{
                        background-color: #0056b3;
                    }}
                    @keyframes fadeIn {{
                        from {{
                            opacity: 0;
                        }}
                        to {{
                            opacity: 1;
                        }}
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1><i class="fas fa-pencil-alt"></i> Pen and Paper Online - Password Reset</h1>
                    <p>Hello Student,</p>
                    <p>You requested a password reset. Click the button below to reset your password:</p>
                    <p><a href="{reset_url}">Reset Password</a></p>
                    <p>If you did not request this, please ignore this email.</p>
                    <p>Alternatively, you can copy and paste the following link into your browser:</p>
                    <p><a href="{reset_url}" style="text-decoration: none; color: #007bff;">{reset_url}</a></p>
                </div>
            </body>
            </html>
            """
            mail.send(msg)
            flash('A password reset link has been sent to your email.', 'success')
        else:
            flash('No account found with that email.', 'danger')
        
        return redirect(url_for('forgot_password'))
    return render_template('forget_password.html')

@app.route('/exam/<int:exam_id>/<int:student_id>')
def conduct_exam(exam_id, student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT questions.id, questions.question, questions.marks
        FROM questions
        WHERE questions.exam_id = %s
    """, (exam_id,))
    questions = cursor.fetchall()

    return render_template('exam.html', questions=questions, student_id=student_id, exam_id=exam_id)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)
        connection = mysql.connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM password_reset_tokens WHERE email = %s AND token = %s ", (email, token))
        token_record = cursor.fetchone()
        if not token_record:
            flash('The reset link is invalid or has expired.', 'danger')
            return redirect(url_for('forgot_password'))
    except:
        flash('The reset link is invalid or has expired.', 'danger')
        return redirect(url_for('forgot_password'))
    
    if request.method == 'POST':
        new_password = request.form['new_password']
        hashed_password = generate_password_hash(new_password)
        cursor.execute("UPDATE register SET password = %s WHERE mail_id = %s", (hashed_password, email))
        cursor.execute("UPDATE password_reset_tokens SET used = TRUE WHERE email = %s", (email,))
        cursor.execute("DELETE FROM password_reset_tokens WHERE email = %s", (email,))
        connection.commit()
        flash('Your password has been reset. You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)

