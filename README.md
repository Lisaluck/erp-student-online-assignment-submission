1. First-Time Setup (For Beginners)

# 1. Open terminal (Linux/Mac) or Command Prompt/PowerShell (Windows)
# 2. Clone the project
git clone https://github.com/yourusername/edumanage.git
cd edumanage

# 3. Create virtual environment
python -m venv venv

# 4. Activate it
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 5. Install requirements
pip install -r requirements.txt
2. Database Setup (Simple Way)

# 1. Create database (SQLite already configured)
python manage.py migrate

# 2. Create admin account (follow prompts)
python manage.py createsuperuser
# (Enter username, email, password when asked)
3. Run the Project

# 1. Start development server
python manage.py runserver

# 2. Open browser and go to:
http://localhost:8000/dashboard
4. For Faculty Accounts
Go to admin panel: http://localhost:8000/admin

Login with your superuser credentials

Click "Users" → Select a user → Under "Permissions" check:

✅ "Staff status"

✅ "Superuser status" (if full access needed)

Click "Save"

5. Adding Test Data (Optional)

# Create sample courses/assignments
python manage.py shell
Then run in Python shell:


from django.contrib.auth.models import User
from core.models import Course, Assignment

# Create test faculty
faculty = User.objects.create_user('prof_x', 'x@school.com', 'test123')
faculty.is_staff = True
faculty.save()

# Create test course
course = Course.objects.create(name="Python Basics", faculty=faculty)

# Create test assignment
Assignment.objects.create(
    course=course,
    title="First Python Program",
    description="Create Hello World program"
)
6. Student Flow (How to Use)
Register at: http://localhost:8000/register

Login at: http://localhost:8000/login

Select your class in profile

View dashboard: http://localhost:8000/dashboard

Click "Submit" on any assignment

Paste GitHub URL like: https://github.com/yourname/python-assignment

7. Faculty Flow
Login with faculty account

Access dashboard: http://localhost:8000/faculty

Create courses/assignments

View submissions at: http://localhost:8000/course/1

8. Troubleshooting
If you see errors:


# If database issues:
python manage.py makemigrations
python manage.py migrate

# If package issues:
pip install -r requirements.txt --force-reinstall

# If server won't start:
kill $(lsof -t -i:8000)  # Linux/Mac
taskkill /F /PID $(netstat -ano | findstr 8000)  # Windows
9. Daily Use Commands

# Start work:
source venv/bin/activate  # Activate environment
python manage.py runserver

# End work:
deactivate  # Leave virtual environment
This covers:
✅ Installation
✅ Account setup
✅ Basic usage
✅ Testing
✅ Troubleshooting

All features should now work including:

Student assignment submission
