📚 LLM Core Concepts – AI Mini Projects Suite 🧠⚙️

🚀 Built as a beginner-friendly collection of Python-based AI experiments demonstrating the core internal working concepts of Large Language Models (LLMs), including Attention Mechanism, Tokenization, Sampling Strategies, Hallucination Behavior, and Semantic Search using Embeddings.

An educational AI project suite that breaks down how modern AI systems like GPT, Gemini, Claude, and LLaMA process language internally using mathematics, probability, embeddings, and retrieval systems.

This project helps students understand AI not as a black box, but as a system built on clear computational and mathematical principles.

📦 Project Overview

This repository contains 5 independent AI mini-projects, each focusing on a core concept used in modern Generative AI systems.

Each project is implemented using Python and widely-used AI/NLP libraries such as NumPy, Hugging Face Transformers, Sentence Transformers, and PyTorch.

The goal is to simulate how real-world LLMs process text, generate responses, and retrieve information.

🧩 Projects Included
1️⃣ Scaled Dot-Product Attention Implementation 🧠⚡

🚀 Built as a beginner-friendly implementation of the Transformer Attention Mechanism using Python and NumPy.

An educational AI project that demonstrates how models like GPT understand relationships between words using Query, Key, and Value matrices.

📖 Key Highlights:
Word embedding creation
Q, K, V matrix generation
QKᵀ attention score computation
Scaling by √dk
Softmax probability calculation
Final attention output generation
🧠 Core Concept:

This project demonstrates the mathematical foundation of the Transformer architecture introduced in the paper “Attention Is All You Need” (2017).

2️⃣ Tokenization and Context Window Cost Analyzer 🧠💬

🚀 Built to demonstrate how text is converted into tokens and how token usage affects cost and context limits in LLMs.

📖 Key Highlights:
BERT tokenizer usage (Hugging Face)
Short vs long text token comparison
Token count calculation
API cost estimation
Context window overflow detection
Subword tokenization visualization
🧠 Core Concept:

Shows how AI models break text into tokens and why long prompts increase cost and processing limits.

3️⃣ Sampling Strategy Experiment 🎲🧠

🚀 Built to explore how AI controls creativity and randomness during text generation.

📖 Key Highlights:
Temperature-based generation
Top-k sampling
Top-p (nucleus) sampling
GPT-2 text generation
Output comparison across configurations
Creativity vs accuracy analysis
🧠 Core Concept:

Explains how decoding strategies control whether AI behaves deterministically or creatively.

4️⃣ Hallucination Detection and Prompt Fix 🧠⚖️

🚀 Built to demonstrate how AI models generate incorrect or fake information and how prompt engineering reduces hallucination.

📖 Key Highlights:
Hallucinated vs corrected outputs
Prompt engineering techniques
Structured JSON-style prompting
Low temperature generation
Legal-domain safety simulation
Before vs After comparison
🧠 Core Concept:

Shows how improper prompts lead to hallucination and how structured constraints improve AI reliability.

5️⃣ Semantic Search Engine Using Embeddings 🧠📚

🚀 Built to demonstrate how modern AI systems understand meaning using embeddings instead of keyword matching.

📖 Key Highlights:
Sentence embeddings (MiniLM model)
Cosine similarity computation
FAQ retrieval system
Semantic vs keyword search comparison
Vector-based similarity matching
Intelligent response retrieval
🧠 Core Concept:

Explains how AI understands meaning using vectors instead of exact words.

🛠️ Technologies Used
Core Stack:
Python 🐍
NumPy
PyTorch
Hugging Face Transformers
Sentence Transformers
Scikit-learn
AI Concepts Covered:
Attention Mechanism
Tokenization
Embeddings
Cosine Similarity
Sampling Strategies
Prompt Engineering
Context Windowing
Semantic Search
🎯 Learning Outcomes

This project suite helps in understanding:

How Transformers work internally
How LLMs tokenize text
How AI generates different types of responses
Why hallucinations happen in AI systems
How embeddings enable semantic understanding
How modern AI search systems work
How prompt design affects model behavior
How real-world LLM APIs operate internally

📂 Project Structure
llm-core-concepts-python/
│
├── attention-mechanism/
├── tokenization-cost-analyzer/
├── sampling-strategy-experiment/
├── hallucination-detection-prompt-fix/
├── semantic-search-embeddings/
│
├── .gitignore
├── README.md
└── requirements.txt

All project execution outputs and screenshots for the complete AI mini-project suite are included in the consolidated report file.

📄 View Full Report (with all screenshots):
👉 report.pdf

🧠 What this report contains:

The report.pdf includes:

✔ All console output screenshots for each project
✔ Step-by-step explanations of each AI concept
✔ Input and output results for every module
✔ Comparative analysis (where applicable)
📌 Projects Covered in Report:
Scaled Dot-Product Attention
Tokenization & Context Window Analyzer
Sampling Strategy Experiment
Hallucination Detection & Prompt Fix
Semantic Search using Embeddings

🚨 Important Notes
All projects are for educational purposes only
Models used (GPT-2, BERT, MiniLM) are lightweight and not production-grade
Real-world LLMs use:
Larger architectures
Retrieval-Augmented Generation (RAG)
Advanced safety systems
Distributed training pipelines

However, the core principles demonstrated here remain the foundation of modern AI systems.

🔮 Future Improvements

This project suite can be extended with:

Streamlit UI dashboard
Real-time LLM API integration
Vector database (FAISS / Pinecone)
Multi-model comparison system
Interactive AI playground
Visualization of attention heatmaps
RAG-based chatbot system
Web-based deployment
👨‍💻 Conclusion

This project suite provides a complete beginner-friendly introduction to how modern Large Language Models work internally.

By implementing attention mechanisms, tokenization, sampling strategies, hallucination detection, and semantic search, it bridges the gap between theory and real-world AI systems.

It is ideal for students who want to understand Generative AI deeply rather than just using it as a black-box tool.

👨‍💻 Author

Dharshini.A

