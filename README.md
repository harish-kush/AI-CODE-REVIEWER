# AI Code Review System 🚀

An automated **AI-powered code review system** that analyzes code changes on every push using **GitHub Actions** and generates structured feedback using **Google Gemini AI**.

The system reviews the latest code changes, generates an **HTML formatted report containing code quality scores and inline suggestions**, and automatically sends the feedback to the developer via **email**.

---

# ✨ Features

* 🔁 **Automated Code Review**

  * Runs automatically on every push using **GitHub Actions**

* 🤖 **AI-Powered Analysis**

  * Uses **Google Gemini API** to analyze code changes

* 📊 **Code Quality Score**

  * Provides a score out of **10 based on best coding practices**

* 🧠 **Inline Suggestions**

  * Highlights issues and suggests improvements

* 📧 **Automated Email Reports**

  * Sends structured **HTML feedback reports**

* ⚡ **Diff-based Review**

  * Reviews only **latest commit changes**

---

# 🛠 Tech Stack

* **Python**
* **GitHub Actions (CI/CD Automation)**
* **Google Gemini API**
* **SMTP Email Automation**
* **Git CLI**

---

# 📂 Project Structure

```
AI-CODE-REVIEW
│
├── .github/
│   └── workflows/
│       └── python-app.yml      # GitHub Actions workflow
│
├── scripts/
│   └── review.py               # Main AI review script
│
├── app.py                      # Optional application entry
├── requirements.txt            # Python dependencies
├── .gitignore
├── venv/                       # Virtual environment (not pushed to repo)
```

---

# ⚙️ How It Works

1️⃣ Developer pushes code to the repository.

2️⃣ **GitHub Actions workflow** is triggered.

3️⃣ The workflow runs the **review.py** script.

4️⃣ The script:

* Extracts latest code changes using `git diff`
* Sends the changes to **Gemini AI**

5️⃣ Gemini analyzes the code and generates:

* Code Quality Score
* Inline Suggestions
* Improvement Recommendations

6️⃣ The response is formatted into **HTML**.

7️⃣ The system sends the **review report via email** using SMTP.

---

# 🔐 Environment Variables

Add the following **GitHub Secrets**:

```
GOOGLE_API_KEY
SENDER_EMAIL
RECEIVER_EMAIL
EMAIL_PASSWORD
```

Path:

```
Repository → Settings → Secrets → Actions
```

---

# 📦 Installation (Local Testing)

Clone the repository:

```
git clone https://github.com/yourusername/AI-CODE-REVIEW.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the review script:

```
python scripts/review.py
```

---

# 🚀 Future Improvements

* Pull Request based code reviews
* GitHub inline comments
* Security vulnerability detection
* Multi-language code analysis
* Slack / Discord notifications
* Web dashboard for review analytics

---

# 📄 Resume Highlight

Developed an **AI-powered automated code review system** using GitHub Actions and Google Gemini API that analyzes commit diffs, generates structured HTML feedback with inline suggestions and quality scoring, and delivers review reports via email.

---

# 👨‍💻 Author

**Harish Kushwaha**

Electronics and Communication Engineering
MANIT BHOPAL
