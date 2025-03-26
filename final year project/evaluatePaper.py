# import docx
# class PaperEvaluator:
#     def evaluate_paper(self,document, keywords, total_marks):
#         document = document.lower()
#         keywords = [keyword.lower() for keyword in keywords]
#         keyword_count = sum(1 for keyword in keywords if keyword in document)
#         obtained_marks = (keyword_count / len(keywords)) * total_marks
#         return round(obtained_marks, 1)
#     def getText(self,filename):
#         doc = docx.Document(filename)
#         fullText = []
#         for para in doc.paragraphs:
#             fullText.append(para.text)
#         return '\n'.join(fullText)
# keywords = ["Cloud Computing", "Digital Age", "Flexible", "Scalable", "Cost-effective", "Data Storage", "Application Development", "Innovation", "Scalability", "Security", "Encryption", "Data Protection", "Remote Work", "Collaboration", "Regulatory Standards", "Data Breaches", "Elasticity", "Competitive", "Performance Optimization", "Agile", "Seamless Collaboration", "Global Market", "Modern Business", "Digital Economy", "On-premise Solutions"]
# total_marks = 10
# paperEvaluator=PaperEvaluator()
# document_text=paperEvaluator.getText("test.docx")
# marks = paperEvaluator.evaluate_paper(document_text, keywords, total_marks)
# print("Marks: ",marks)
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
sentence1 = "Achieving success requires perseverance and the ability to adapt"
sentence2 = "Requires perseverance and the ability to adapt"
embedding1 = model.encode([sentence1])
embedding2 = model.encode([sentence2])
similarity = cosine_similarity(embedding1, embedding2)
print(f"Similarity: {similarity[0][0]*100}%")