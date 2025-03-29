# **EduManage - AI-Powered College ERP System**

## 🚀 **Overview**

EduManage is an advanced AI-driven **College ERP System** designed to streamline academic workflows, enhance faculty productivity, and improve student learning experiences. The platform offers **AI-based grading**, **assignment submission**, and real-time faculty-student interaction to optimize education management.

## ✨ **Key Features**

### 🔹 **Role-Based Dashboards**

- **Admin Panel:** Manage classes, courses, and faculty assignments.
- **Faculty Dashboard:**
  - View assigned classes and courses.
  - Add assignments, study materials, and notices.
  - Monitor student submissions with AI-generated grading.
- **Student Dashboard:**
  - Submit assignments via GitHub repository links.
  - Access study materials and notices.
  - View AI-evaluated grades instantly.

### 🤖 **AI-Powered Features**

- **AI-based Assignment Grading**: Automated and intelligent grading system for submitted assignments.
- **Automated Notifications**: Students receive emails for new assignments, study materials, and notices.

### 🔒 **Secure Authentication**

- Role-based login for **Admin, Faculty, and Students**.
- Password encryption and secure session management.

## 🛠 **Tech Stack**

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be changed to MySQL/PostgreSQL for production)
- **AI Integration:** AI-based grading system
- **Deployment:** Can be deployed on **Vercel** (Frontend) & **Railway/Render** (Backend)

## ⚡ **Installation & Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/edumanage.git
   cd edumanage
   ```
2. **Create a virtual environment & activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser** (for Admin access)
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the server**
   ```bash
   python manage.py runserver
   ```
7. **Access the application**
   - Open `http://127.0.0.1:8000/` in your browser.
   - Login with admin, faculty, or student credentials.

## 📜 **API Endpoints (For Developers)**

| Endpoint            | Method | Description                |
| ------------------- | ------ | -------------------------- |
| `/api/login/`       | POST   | User authentication        |
| `/api/courses/`     | GET    | List available courses     |
| `/api/assignments/` | POST   | Faculty adds assignments   |
| `/api/submissions/` | POST   | Student submits assignment |
| `/api/grades/`      | GET    | Fetch AI-generated grades  |

## 🚀 **Deployment on Vercel (Frontend) & Render/Railway (Backend)**

### **Frontend Deployment (Vercel)**

1. Install Vercel CLI
   ```bash
   npm install -g vercel
   ```
2. Deploy frontend (if using React/Next.js)
   ```bash
   vercel
   ```

### **Backend Deployment (Render/Railway)**

1. Push code to GitHub.
2. Create a new Django project on **Render/Railway**.
3. Add necessary environment variables (e.g., `DATABASE_URL`, `SECRET_KEY`).
4. Deploy and get the backend API URL.

## 🎯 **Future Enhancements**

- AI-based plagiarism detection for assignments.
- Advanced analytics for student performance tracking.
- Mobile app integration for on-the-go access.

## 🤝 **Contributing**

We welcome contributions! Feel free to fork this repository and submit a pull request.

## 📩 **Contact**

For queries or support, reach out via unstop 

---

### ⭐ **If you like this project, don't forget to give it a star!** 🌟


