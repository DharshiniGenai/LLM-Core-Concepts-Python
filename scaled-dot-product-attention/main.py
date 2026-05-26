import numpy as np

# ==================================================
# ASSIGNMENT 1 - SCALED DOT PRODUCT ATTENTION
# ==================================================

np.set_printoptions(precision=2, suppress=True)

# --------------------------------------------------
# Step 1: Input Sentence
# --------------------------------------------------

sentence = "AI transforms the world"
words = sentence.split()

print("=" * 60)
print("INPUT SENTENCE")
print("=" * 60)
print(words)

# --------------------------------------------------
# Step 2: Create Word Embeddings
# --------------------------------------------------
# Each word gets a 4-dimensional embedding vector

embeddings = np.array([
    [0.62, 0.11, 0.45, 0.72],   # AI
    [0.91, 0.53, 0.27, 0.34],   # transforms
    [0.15, 0.87, 0.64, 0.29],   # the
    [0.73, 0.21, 0.88, 0.55]    # world
])

print("\n" + "=" * 60)
print("WORD EMBEDDINGS")
print("=" * 60)
print(embeddings)

# --------------------------------------------------
# Step 3: Create Weight Matrices
# --------------------------------------------------

np.random.seed(42)

Wq = np.random.rand(4, 4)
Wk = np.random.rand(4, 4)
Wv = np.random.rand(4, 4)

# --------------------------------------------------
# Step 4: Compute Query, Key, Value Matrices
# --------------------------------------------------

Q = embeddings @ Wq
K = embeddings @ Wk
V = embeddings @ Wv

print("\n" + "=" * 60)
print("QUERY MATRIX (Q)")
print("=" * 60)
print(Q)

print("\n" + "=" * 60)
print("KEY MATRIX (K)")
print("=" * 60)
print(K)

print("\n" + "=" * 60)
print("VALUE MATRIX (V)")
print("=" * 60)
print(V)

# --------------------------------------------------
# Step 5: Compute Raw Attention Scores (QK^T)
# --------------------------------------------------

raw_scores = Q @ K.T

print("\n" + "=" * 60)
print("RAW QK^T MATRIX")
print("=" * 60)
print(raw_scores)

# --------------------------------------------------
# Step 6: Scale the Scores
# --------------------------------------------------

dk = K.shape[1]

scaled_scores = raw_scores / np.sqrt(dk)

print("\n" + "=" * 60)
print("SCALED SCORES")
print("=" * 60)
print(scaled_scores)

# --------------------------------------------------
# Step 7: Apply Softmax Function
# --------------------------------------------------

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

attention_probs = softmax(scaled_scores)

print("\n" + "=" * 60)
print("SOFTMAX PROBABILITIES")
print("=" * 60)
print(attention_probs)

# --------------------------------------------------
# Step 8: Final Attention Output
# --------------------------------------------------

attention_output = attention_probs @ V

print("\n" + "=" * 60)
print("FINAL ATTENTION OUTPUT VECTOR")
print("=" * 60)
print(attention_output)

# --------------------------------------------------
# Step 9: Explanation
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXPLANATION")
print("=" * 60)
print("1. Word embeddings represent each word numerically.")
print("2. Q, K, and V matrices are generated using weight matrices.")
print("3. QK^T calculates similarity between words.")
print("4. Scores are scaled using sqrt(dk).")
print("5. Softmax converts scores into probabilities.")
print("6. Final attention output is computed using probabilities and V matrix.")