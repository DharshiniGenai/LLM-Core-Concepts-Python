from transformers import pipeline

print("=" * 70)
print("HALLUCINATION DETECTION AND PROMPT FIX")
print("=" * 70)

# Load text generation model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# ============================================================
# BEFORE PROMPT FIX
# ============================================================

before_prompt = "List Supreme Court AI judgments in India 2025."

print("\nBEFORE PROMPT FIX")
print("=" * 70)

before_output = generator(
    before_prompt,
    max_new_tokens=80,
    temperature=1.0,
    do_sample=True
)

print(before_output[0]["generated_text"])

# ============================================================
# AFTER PROMPT FIX
# ============================================================

after_prompt = """
You are a factual AI assistant.

Rules:
1. Do NOT invent legal cases or citations.
2. If verified information is unavailable, clearly say so.
3. Only provide confirmed information.
4. Return output strictly in JSON format.

Question:
List verified Supreme Court AI judgments in India in 2025.
"""

print("\nAFTER PROMPT FIX")
print("=" * 70)

after_output = generator(
    after_prompt,
    max_new_tokens=80,
    temperature=0.2,
    do_sample=True
)

print(after_output[0]["generated_text"])

# ============================================================
# OBSERVATION
# ============================================================

print("\n" + "=" * 70)
print("OBSERVATION")
print("=" * 70)

print("""
Before Prompt Fix:
- The model may generate hallucinated legal acts,
  fake citations, or unverified judgments.
- High randomness increases misinformation risk.

After Prompt Fix:
- Structured prompting improves reliability.
- Low temperature reduces randomness.
- JSON constraints encourage organized output.
- The model is more likely to admit uncertainty
  instead of inventing fake legal information.
""")

# ============================================================
# FINAL RECOMMENDATION
# ============================================================

print("=" * 70)
print("FINAL RECOMMENDATION")
print("=" * 70)

print("""
For legal, medical, and financial systems:

- Use strict prompts
- Use low temperature
- Ask for structured JSON output
- Instruct the model to avoid assumptions
- Require verified information only

This helps reduce hallucinations and improves
trustworthiness in critical AI applications.
""")

print("=" * 70)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 70)