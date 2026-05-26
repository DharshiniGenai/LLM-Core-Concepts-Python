from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ============================================================
# SEMANTIC SEARCH ENGINE USING EMBEDDINGS
# ============================================================

print("=" * 70)
print("SEMANTIC SEARCH ENGINE USING EMBEDDINGS")
print("=" * 70)

# ============================================================
# FAQ DATASET
# ============================================================

faq_data = [
    {
        "question": "How can I reset my password?",
        "answer": "To reset your password, click on Forgot Password and follow the instructions."
    },
    {
        "question": "How do I create a new account?",
        "answer": "Click on Sign Up and fill in your personal details to create an account."
    },
    {
        "question": "How can I update my email address?",
        "answer": "Go to account settings and update your registered email address."
    },
    {
        "question": "How do I contact customer support?",
        "answer": "You can contact customer support through email or live chat."
    },
    {
        "question": "How can I change my profile picture?",
        "answer": "Open profile settings and upload a new profile image."
    },
    {
        "question": "How do I delete my account?",
        "answer": "Visit account settings and select Delete Account."
    },
    {
        "question": "How can I track my order?",
        "answer": "Use the order tracking option available in your dashboard."
    },
    {
        "question": "How do I cancel my subscription?",
        "answer": "Go to subscription settings and click Cancel Subscription."
    },
    {
        "question": "How can I enable two-factor authentication?",
        "answer": "Enable two-factor authentication from the security settings page."
    },
    {
        "question": "How do I download my invoice?",
        "answer": "Invoices can be downloaded from the billing section."
    }
]

# ============================================================
# USER QUERY
# ============================================================

user_query = "How can I reset my password?"

print("\nUSER QUERY:")
print(user_query)

# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

print("\nLoading embedding model...")

model = SentenceTransformer('all-MiniLM-L6-v2')

# ============================================================
# GENERATE FAQ EMBEDDINGS
# ============================================================

faq_questions = [faq["question"] for faq in faq_data]

faq_embeddings = model.encode(faq_questions)

# ============================================================
# GENERATE QUERY EMBEDDING
# ============================================================

query_embedding = model.encode([user_query])

# ============================================================
# CALCULATE COSINE SIMILARITY
# ============================================================

similarity_scores = cosine_similarity(
    query_embedding,
    faq_embeddings
)[0]

# ============================================================
# PRINT SIMILARITY SCORES
# ============================================================

print("\n" + "=" * 70)
print("SIMILARITY SCORES")
print("=" * 70)

for i, score in enumerate(similarity_scores):
    print(f"FAQ {i+1}: {score:.4f}")
    print(f"Question: {faq_data[i]['question']}")
    print("-" * 70)

# ============================================================
# FIND BEST MATCH
# ============================================================

best_match_index = np.argmax(similarity_scores)

best_question = faq_data[best_match_index]["question"]
best_answer = faq_data[best_match_index]["answer"]
best_score = similarity_scores[best_match_index]

# ============================================================
# PRINT TOP MATCH
# ============================================================

print("\n" + "=" * 70)
print("TOP MATCH")
print("=" * 70)

print(f"Best Matching Question:")
print(best_question)

print(f"\nSimilarity Score:")
print(f"{best_score:.4f}")

print(f"\nBest Answer:")
print(best_answer)

# ============================================================
# SIMPLE KEYWORD SEARCH
# ============================================================

print("\n" + "=" * 70)
print("KEYWORD SEARCH RESULT")
print("=" * 70)

keyword_match_found = False

query_words = set(user_query.lower().split())

for faq in faq_data:
    faq_words = set(faq["question"].lower().split())

    if query_words == faq_words:
        keyword_match_found = True

        print("Exact Keyword Match Found:")
        print(faq["question"])
        print(faq["answer"])

if not keyword_match_found:
    print("No exact match found.")

# ============================================================
# COMPARISON
# ============================================================

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("""
Semantic Search:
- Understands meaning and context
- Uses embeddings and cosine similarity
- Can match similar sentences even with different wording
- Better for intelligent AI systems

Keyword Search:
- Matches exact words only
- Cannot understand sentence meaning
- Fails if wording changes
- Simpler but less intelligent
""")

# ============================================================
# CONCLUSION
# ============================================================

print("=" * 70)
print("CONCLUSION")
print("=" * 70)

print("""
Embedding-based semantic search captures contextual meaning
better than traditional keyword search.

Even if users phrase questions differently, semantic embeddings
can still retrieve the most relevant answer using similarity scores.

This is one of the core technologies used in:
- AI Chatbots
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- AI Search Engines
- Modern LLM Applications
""")

print("=" * 70)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 70)