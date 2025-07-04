# 🍽️ AI Menu Crafter

This Streamlit application uses Generative AI (Gemma 2B via Ollama) to suggest unique restaurant names and curated food menus based on the selected cuisine.

## 🚀 Features:
- Choose from multiple global cuisines (Indian, Italian, Mexican, etc.)
- Automatically generates a restaurant name
- Suggests a menu of items as a comma-separated list
- Powered by LangChain’s SequentialChain with prompt templating

## 🧠 How it Works:
- **LLM Prompt 1:** Suggests a unique restaurant name based on cuisine type.
- **LLM Prompt 2:** Based on the name, generates food menu items.
- No extra commentary or descriptions are included—clean, direct outputs.

## 🛠️ Tech Stack:
- Python
- Streamlit
- LangChain
- Ollama (Gemma 2B)(you can use any other llm-model or llm-runtime , ollama is local LLM_runtime)
