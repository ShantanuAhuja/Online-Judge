# 🧠 **Online Judge Platform**

An advanced **Online Coding Judge System** built using Django. This platform enables users to **solve coding problems**, **submit solutions**, **view verdicts**, and **track their progress** with dynamic and interactive features, similar to popular platforms like **LeetCode**, **Codeforces**, and **HackerRank**.

---

## 🔧 **Core Features**

- 🗂 **Problem Listing and Details View**
- ✅ **Code Submission and Verdict System**
- 📈 **User Submissions History**
- 🏆 **Leaderboard with Dynamic Scoring**
- 🔐 **Authentication & Authorization**
- ⚙️ **Settings and User Info Pages**
- 🛠 **Multiple Language Support with Boilerplate Code**
- 🖼 **Elegant UI Templates using Django Templates**

---

## 🧩 **App-wise Functionality Breakdown**

---

## 📝 **`problems` App**

### 📄 **`renderProblemsApi(request)`**

**Function**: Fetches and displays the complete list of problems.

**Route**: `/problems/`

**Template**: `problemsPage.html`

**Usage**:
- Queries the `Problem` model.
- Passes data to the frontend for display.

---

### 🔍 **`renderProblemsDetailsApi(request, name)`**

**Function**: Displays detailed information for a selected problem.

**Route**: `/problems/<name>/`

**Template**: `problemsDetails.html`

**Usage**:
- Fetches the problem based on the `name`.
- Loads **description**, **sample test cases**, **tags**, and **language-wise boilerplate code**.
- Displays in a user-friendly format for solving.

**Languages Supported with Boilerplate**:
- C
- C++
- Java
- Python

---

## 📤 **`submission` App**

### 📂 **`showUserSubmission(request)`**

**Function**: Shows the latest 10 code submissions by the logged-in user.

**Route**: `/submissions/`

**Template**: `userSubmissions.html`

**Usage**:
- Fetches the `CodeSubmission` for `request.user`.
- Orders them by `timestamp`.
- Renders a list for review.

---

### 📘 **`showParticularSubmission(request, id)`**

**Function**: Displays the content and details of a specific code submission.

**Route**: `/submissions/<id>/`

**Template**: `particularCodeSubmission.html`

**Usage**:
- Opens the file from the `submission.code` path.
- Reads and sends the code content to the template.
- If the file doesn’t exist, returns a 404 or file read error.

---

### 🏅 **`showLeaderboard(request)`**

**Function**: Displays the platform leaderboard with scores based on accepted submissions.

**Route**: `/leaderboard/`

**Template**: `leaderboard.html`

**Usage**:
- Iterates over all users.
- Counts unique problems where the user got “Accepted” verdict.
- Calculates score as: `Number of Unique Accepted Problems × 100`.
- Sorts and renders results.

---

## 🛠 **Additional Utilities & Design Choices**

- 🧪 **Test Cases** and **Verdict Mapping** via `Problem.testcases` and `CodeSubmission.verdict`
- 🔒 **LoginRequiredDecorator** to restrict access
- 📁 **File-based code storage and retrieval**
- 🎨 **Django templates** with condition-based rendering
- 🧾 **Logs** and **prints** (e.g., `print(description)`) to aid debugging

---

## 🏗 **File Structure Overview**

. ├── problems/ │ ├── models.py │ ├── views.py │ ├── templates/ │ │ ├── problemsPage.html │ │ └── problemsDetails.html │ ├── submissions/ │ ├── models.py │ ├── views.py │ ├── templates/ │ │ ├── userSubmissions.html │ │ └── particularCodeSubmission.html │ ├── leaderboard/ │ └── views.py │ └── leaderboard.html


---

## 🚀 **Future Enhancements**

- 🌍 Add code execution engine using Docker or third-party services
- 📊 Add real-time leaderboard updates and badges
- 🧠 Integrate **LLM-based code hints** or **AI-suggested solutions**
- 🔄 Add support for version control in submissions

---

## 💡 **About This Project**

This project was built to learn and implement:
- Real-world **Django project structure**
- **Backend logic separation** per module
- **ORM usage** for relational problem-user-submission modeling
- Custom user features like **code tracking**, **leaderboard**, etc.

---

## 👤 **Authored & Maintained By**

- 💻 [Your Name or Username]
- 🛠 **Tech Stack**: Python, Django, SQLite/PostgreSQL, HTML/CSS, Bootstrap

---



