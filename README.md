# Streamlit Practice App

This is a **Streamlit** web app showcasing various interactive UI elements, data visualizations, and advanced Streamlit features. It's intended as a hands-on practice project for learning and demonstrating Streamlit capabilities.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- `streamlit`, `pandas`, `numpy`

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the App

```bash
python -m streamlit run app.py
```

## 🧭 App Categories Overview

This project contains four types of Streamlit apps, each demonstrating different capabilities and use cases:

### 1. Fundamentals
These scripts demonstrate fundamental Streamlit concepts like layout, widgets, and user interaction. Includes:
- `app.py`, `main_page.py`, `page_2.py`, `page_3.py`

### 2. Single Page App
A standalone visualization app:
- `uber_pickups.py`: Visualizes NYC Uber pickups using interactive maps and filters.

### 3. Multipage App
A modular app using Streamlit's multipage support:
- `Hello.py`: Entry point.
- `pages/`: Demos on plotting, mapping, and data table interaction.

### 4. Chat and LLM Apps
Demonstrates interactive NLP/chat capabilities using the OpenAI API:
- `1-echo_bot.py`: A basic chatbot that repeats back the user's message.
- `2-simple_chat.py`: Adds multi-turn memory to the chatbot using session state.
- `3-chatgpt_clone.py`: A ChatGPT-style interface with streaming responses and model selection.

## 📁 Project Structure

```text
.
├── 1. Fundamentals/
│   ├── app.py
│   ├── main_page.py
│   ├── page_2.py
│   └── page_3.py
├── 2. Single Page App/
│   └── uber_pickups.py
├── 3. Multipage App/
│   ├── Hello.py
│   └── pages/
│       ├── 1_📈_Plotting_Demo.py
│       ├── 2_🌍_Mapping_Demo.py
│       └── 3_📊_DataFrame_Demo.py
├── 4. Chat and LLM Apps/
│   ├── 1-echo_bot.py
│   ├── 2-simple_chat.py
│   └── 3-chatgpt_clone.py
└── requirements.txt
```
