import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
def get_synsets(word):
    return wn.synsets(word)

def word_similarity(word1, word2):
    synsets1 = get_synsets(word1)
    synsets2 = get_synsets(word2)
    
    if not synsets1 or not synsets2:
        return 0  # Return 0 if no synsets are found for either word

    # Calculate the maximum similarity between all pairs of synsets
    max_sim = 0
    for syn1 in synsets1:
        for syn2 in synsets2:
            similarity = syn1.wup_similarity(syn2)  # Wu-Palmer similarity
            if similarity is not None:
                max_sim = max(max_sim, similarity)
    
    return max_sim

# Function to calculate the cosine similarity between two sentences
def cosine_similarity_of_sentences(sentence1, sentence2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

# Function to compare two sentences semantically
def are_sentences_semantically_equal(sentence1, sentence2, method="wordnet", threshold=0.7):
    if method == "wordnet":
        # Tokenize the sentences into words
        words1 = word_tokenize(sentence1)
        words2 = word_tokenize(sentence2)

        # Calculate average similarity between all word pairs
        total_similarity = 0
        count = 0

        for word1 in words1:
            for word2 in words2:
                similarity = word_similarity(word1, word2)
                total_similarity += similarity
                count += 1

        # Calculate the average similarity
        avg_similarity = total_similarity / count if count > 0 else 0
        print(f"Average WordNet Similarity: {avg_similarity}")
        
        # Compare with the threshold
        return avg_similarity >= threshold

    elif method == "cosine":
        # Use cosine similarity between the two sentences
        similarity = cosine_similarity_of_sentences(sentence1, sentence2)
        print(f"Cosine Similarity: {similarity}")
        
        # Compare with the threshold
        return similarity >= threshold

    else:
        print("Invalid method chosen. Please choose 'wordnet' or 'cosine'.")
        return False

# Example sentences
sentence1 = "I am learning how to use Python programming"
sentence2 = "I am studying how to work with Python code"

# Choose method: "wordnet" or "cosine"
method = "cosine"  # You can switch between "wordnet" and "cosine"
threshold = 0.4 # Threshold for similarity

if are_sentences_semantically_equal(sentence1, sentence2, method=method, threshold=threshold):
    print("The sentences are semantically equal!")
else:
    print("The sentences are not semantically equal.")
