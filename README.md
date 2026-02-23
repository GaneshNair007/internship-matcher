# 🎯 Internship Skill Matcher

A professional web application designed to help students match their technical skills with real-world internship opportunities from top companies like **Zscaler, Amazon, Visa, and Snowflake**.

## 🚀 Live Demo
[Insert your Streamlit Cloud URL here]

## ✨ Features
* **Age-Verified Access:** Integrated age-gate to ensure users are 18+ and eligible for legal internships.
* **Skill Matching Engine:** Uses Python and Pandas to calculate a match score based on user-provided skills and job requirements.
* **Interactive Skill Gap Analysis:** A Radar (Spider) Chart powered by Plotly that visually compares your current skills against company requirements.
* **Pure Black Theme:** A custom, high-contrast dark UI with glassmorphism effects for a modern look.
* **Location Filtering:** Includes specific roles for locations like **Pune** and international hubs.

## 🛠️ Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Data Handling:** Pandas
* **Visualization:** Plotly (Radar Charts)
* **Styling:** Custom CSS & HTML

## 📊 How it Works
1. **User Profile:** Enter your name and birth date in the sidebar to verify eligibility.
2. **Skill Entry:** Input your technical skills (e.g., Python, SQL, Machine Learning).
3. **Matching:** The app scans `output(1).csv` to find companies that require those specific tags.
4. **Analysis:** Select a company from the dropdown to see a visual "Skill Gap" graph.

## 📁 Project Structure
* `work.py`: The main application logic and UI code.
* `output(1).csv`: The internship dataset containing company names, roles, and skill tags.
* `requirements.txt`: List of dependencies (Streamlit, Pandas, Plotly) required for deployment.

## 🔧 Installation & Local Setup
To run this project on your local machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/GaneshNair007/internship-matcher.git](https://github.com/GaneshNair007/internship-matcher.git)
