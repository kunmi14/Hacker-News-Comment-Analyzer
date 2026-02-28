# 📰 Hacker News Comment Analyzer

This project is a simple but practical web scraping script that fetches a Hacker News discussion thread, extracts user comments, and analyzes them for programming language mentions.

Instead of just scraping data, this script focuses on extracting meaningful insights from conversations — specifically counting how often certain programming languages are mentioned and identifying Python-related comments.

---

## 🚀 What This Project Does

- Fetches a Hacker News discussion thread
- Extracts top-level comments
- Counts mentions of selected programming languages:
  - Python
  - JavaScript
  - TypeScript
  - DevOps
  - Ruby
  - Java
- Prints:
  - A keyword frequency summary
  - All Python-related comments found in the thread

---

## 🧠 Why I Built This

I wanted to practice:

- Writing clean, modular Python code
- Structuring scraping logic into reusable functions
- Handling HTTP errors gracefully
- Performing simple text analysis
- Working with sets and dictionaries for efficient keyword tracking

This project reflects how I approach real-world problems:
Break them into small functions, keep the code readable, and focus on extracting useful insights — not just raw data.

---

## 🛠 Tech Stack

- Python 3
- requests – for sending HTTP requests
- BeautifulSoup (bs4) – for parsing HTML
- lxml – parser engine
- typing – for better type hints and readability

---

## 📂 Project Structure

The script is divided into clear functional blocks:

### 1️⃣ `fetch_url`
Fetches the webpage using custom headers and returns a parsed BeautifulSoup object.

### 2️⃣ `get_comments`
Extracts top-level comments from the page.

### 3️⃣ `get_keywords`
Counts keyword mentions and collects Python-related comments.

### 4️⃣ `main`
Controls the program flow:
- Fetch
- Extract
- Analyze
- Print results

---

## 📊 Example Output

```
{'python': 12, 'javascript': 8, 'typescript': 4, 'devops': 3, 'ruby': 1, 'java': 5}

Found 7 python related comments

1., python is great for scripting and automation...
--------------------------------------------------------------------------------
```

---

## 🧩 What This Demonstrates

- Clean function design
- Error handling with try/except
- Defensive programming (checking for None values)
- Text cleaning and normalization
- Keyword frequency tracking
- Real-world HTML parsing

---

## 📈 Possible Improvements

- Add sentiment analysis to comments
- Store results in JSON or CSV
- Add concurrency for faster scraping
- Accept thread ID as CLI argument
- Visualize keyword trends with matplotlib
- Expand to analyze multiple threads

---

## ⚠️ Disclaimer

This project is for educational purposes. Always respect website policies and avoid excessive scraping that may affect service availability.

---

If you’re exploring web scraping, text processing, or lightweight data analysis with Python, this is a solid example of how to structure your code cleanly and professionally.
