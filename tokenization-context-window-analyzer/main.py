from transformers import AutoTokenizer

# ============================================================
# TOKENIZATION AND CONTEXT WINDOW COST ANALYZER
# ============================================================

print("=" * 60)
print("TOKENIZATION AND CONTEXT WINDOW COST ANALYZER")
print("=" * 60)

# ------------------------------------------------------------
# LOAD TOKENIZER
# ------------------------------------------------------------

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# ------------------------------------------------------------
# INPUT TEXTS
# ------------------------------------------------------------

short_text = "Machine learning is powerful."

long_text = """
Machine learning is a branch of artificial intelligence that enables computers
to learn patterns from data and make predictions or decisions without being
explicitly programmed. It is widely used in recommendation systems, chatbots,
image recognition, fraud detection, healthcare, autonomous vehicles, and many
other real-world applications. Machine learning models improve automatically
through experience and training data. Popular techniques include supervised
learning, unsupervised learning, and reinforcement learning. Modern AI systems
such as large language models and generative AI are built using advanced
machine learning and deep learning architectures.
"""

# ------------------------------------------------------------
# TOKENIZATION
# ------------------------------------------------------------

short_tokens = tokenizer.tokenize(short_text)
long_tokens = tokenizer.tokenize(long_text)

# ------------------------------------------------------------
# TOKEN COUNTS
# ------------------------------------------------------------

short_token_count = len(short_tokens)
long_token_count = len(long_tokens)

# ------------------------------------------------------------
# COST ESTIMATION
# ------------------------------------------------------------

cost_per_1000_tokens = 0.002

short_cost = (short_token_count / 1000) * cost_per_1000_tokens
long_cost = (long_token_count / 1000) * cost_per_1000_tokens

# ------------------------------------------------------------
# CONTEXT WINDOW LIMIT
# ------------------------------------------------------------

context_window_limit = 50

short_overflow = short_token_count > context_window_limit
long_overflow = long_token_count > context_window_limit

# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SHORT TEXT")
print("=" * 60)

print("\nInput:")
print(short_text)

print("\nTokens:")
print(short_tokens)

print("\nToken Count:")
print(short_token_count)

print("\nEstimated Cost (@$0.002 per 1K tokens):")
print(f"${short_cost:.8f}")

print("\nContext Window Limit:")
print(context_window_limit)

print("\nOverflow Detected:")
print(short_overflow)

# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LONG TEXT")
print("=" * 60)

print("\nInput:")
print(long_text)

print("\nTokens:")
print(long_tokens)

print("\nToken Count:")
print(long_token_count)

print("\nEstimated Cost (@$0.002 per 1K tokens):")
print(f"${long_cost:.8f}")

print("\nContext Window Limit:")
print(context_window_limit)

print("\nOverflow Detected:")
print(long_overflow)

# ------------------------------------------------------------
# COMPARISON
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("COMPARISON SUMMARY")
print("=" * 60)

print(f"\nShort Text Tokens : {short_token_count}")
print(f"Long Text Tokens  : {long_token_count}")

print(f"\nShort Text Cost : ${short_cost:.8f}")
print(f"Long Text Cost  : ${long_cost:.8f}")

print("\nObservation:")
print("Longer text consumes more tokens and increases API cost.")
print("If token count exceeds the context window limit, overflow occurs.")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)