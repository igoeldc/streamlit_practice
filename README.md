# Streamlit Practice App

This is a **Streamlit** web app showcasing various interactive UI elements, data visualizations, and advanced Streamlit features. It's intended as a hands-on practice project for learning and demonstrating Streamlit capabilities.

## 📦 Features

### Basic Concepts

- **DataFrame Display**: Shows static and styled pandas DataFrames.
- **Charts**: Line chart and map using random data.
- **Widgets**:
  - Slider for calculating square values
  - Text input
  - Checkbox to toggle data
  - Selectbox for options
- **Sidebar UI**: Includes a selectbox and a slider.
- **Layout**: Two-column layout with buttons and radio selections.
- **Progress Bar**: Simulates iterative progress updates.

### Advanced Concepts

- **Caching**: Placeholder for long-running cached functions.
- **Session State**: Tracks interactions like page reload count.
- **Color Picker**: Interactive point coloring in a scatter chart.
- **Connections**: (Commented out) Example for database querying.
- **Pages**: Navigates across multiple pages (e.g., `main_page.py`, `page_2.py`, etc.)
- **Static Files**: Displays an image from the `static` folder.

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

## 📁 Project Structure

```text
.
├── app.py
├── main_page.py
├── page_2.py
├── page_3.py
├── static/
│   └── cat.png
└── requirements.txt
```
