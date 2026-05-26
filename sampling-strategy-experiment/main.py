from transformers import pipeline

print("=" * 70)
print("SAMPLING STRATEGY EXPERIMENT")
print("=" * 70)

# Load text generation pipeline
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Input Prompt
prompt = "Explain Artificial Intelligence in simple terms."

print("\nPROMPT:")
print(prompt)

print("\n" + "=" * 70)
print("TEMPERATURE = 0.1")
print("=" * 70)

low_temp_output = generator(
    prompt,
    max_new_tokens=50,
    temperature=0.1,
    do_sample=True
)

print(low_temp_output[0]["generated_text"])

print("\n" + "=" * 70)
print("TEMPERATURE = 1.0")
print("=" * 70)

high_temp_output = generator(
    prompt,
    max_new_tokens=50,
    temperature=1.0,
    do_sample=True
)

print(high_temp_output[0]["generated_text"])

print("\n" + "=" * 70)
print("TOP-K = 10")
print("=" * 70)

top_k_output = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    top_k=10
)

print(top_k_output[0]["generated_text"])

print("\n" + "=" * 70)
print("TOP-P = 0.9")
print("=" * 70)

top_p_output = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    top_p=0.9
)

print(top_p_output[0]["generated_text"])

print("\n" + "=" * 70)
print("COMPARISON SUMMARY")
print("=" * 70)

print("""
Temperature = 0.1
- Produces stable and predictable responses
- Less creativity
- More accurate and focused

Temperature = 1.0
- Produces more creative and diverse responses
- Higher randomness
- Better for storytelling and brainstorming

Top-k Sampling
- Limits token selection to top probable words
- Produces controlled creativity
- Helps reduce strange outputs

Top-p Sampling
- Dynamically selects probable tokens
- Produces more natural language generation
- Balances creativity and coherence
""")

print("=" * 70)
print("FINAL RECOMMENDATION")
print("=" * 70)

print("""
Recommended Usage:

1. Legal Systems
- Use Low Temperature (0.1)
- Use Smaller Top-k
Reason:
Legal systems require accurate, deterministic,
and consistent outputs with minimal randomness.

2. Creative Writing Systems
- Use Higher Temperature (1.0)
- Use Top-p Sampling
Reason:
Creative applications benefit from diverse,
imaginative, and flexible text generation.
""")

print("=" * 70)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 70)