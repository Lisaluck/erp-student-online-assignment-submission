from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, StudyMaterial, Assignment, Submission, Class, User
from .forms import CourseForm, StudyMaterialForm, AssignmentForm, SubmissionForm, UserRegisterForm
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Program


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    available_classes = Class.objects.all().order_by('program__name', 'year', 'section')
    return render(request, 'profile.html', {
        'available_classes': available_classes
    })


@login_required
def dashboard(request):
    if request.user.is_student:
        student_class = request.user.student_class

        if student_class:
            # Get courses and assignments for student's class
            courses = Course.objects.filter(class_associated=student_class)
            assignments = Assignment.objects.filter(course__in=courses)

            # Get submission status
            submissions = Submission.objects.filter(
                assignment__in=assignments,
                student=request.user
            )
            submission_status = {sub.assignment_id: True for sub in submissions}

            return render(request, 'student_dashboard.html', {
                'student_class': student_class,
                'courses': courses,
                'assignments': assignments,
                'submission_status': submission_status,
                'program_name': student_class.program.name if student_class else None,
                'year': student_class.year if student_class else None,
                'section': student_class.section if student_class else None
            })

        # If no class selected
        messages.warning(request, "Please select your class from profile")
        return render(request, 'student_dashboard.html')

    # Faculty dashboard logic
    return render(request, 'faculty_dashboard.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_course(request):
    if not request.user.is_faculty:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.faculty = request.user
            course.save()
            messages.success(request, 'Course created successfully!')
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    study_materials = StudyMaterial.objects.filter(course=course)
    assignments = Assignment.objects.filter(course=course)

    if request.user.is_student:
        submissions = Submission.objects.filter(assignment__in=assignments, student=request.user)
        submission_status = {sub.assignment.id: sub for sub in submissions}
        return render(request, 'student_course_detail.html', {
            'course': course,
            'study_materials': study_materials,
            'assignments': assignments,
            'submission_status': submission_status
        })
    else:
        submissions = {}
        for assignment in assignments:
            submissions[assignment.id] = Submission.objects.filter(assignment=assignment)
        return render(request, 'faculty_course_detail.html', {
            'course': course,
            'study_materials': study_materials,
            'assignments': assignments,
            'submissions': submissions
        })


@login_required
def add_study_material(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            study_material = form.save(commit=False)
            study_material.course = course
            study_material.save()
            messages.success(request, 'Study material added successfully!')
            return redirect('course_detail', course_id=course.id)
    else:
        form = StudyMaterialForm()
    return render(request, 'add_study_material.html', {'form': form, 'course': course})


@login_required
def create_assignment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = course
            assignment.save()
            messages.success(request, 'Assignment created successfully!')
            return redirect('course_detail', course_id=course.id)
    else:
        form = AssignmentForm()
    return render(request, 'create_assignment.html', {'form': form, 'course': course})


@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user

            # Here you would add AI grading logic
            submission.ai_feedback = "Sample AI feedback - this would be generated by your AI system"
            submission.marks = 85.5  # Sample marks from AI grading

            submission.save()
            messages.success(request, 'Assignment submitted successfully!')
            return redirect('course_detail', course_id=assignment.course.id)
    else:
        form = SubmissionForm()
    return render(request, 'submit_assignment.html', {'form': form, 'assignment': assignment})

def custom_logout(request):
    logout(request)
    return redirect('login')


from django.contrib import messages
from django.shortcuts import redirect


@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)

    if request.method == 'POST':
        github_url = request.POST.get('github_url')

        # Validate GitHub URL
        if not github_url or 'github.com' not in github_url:
            messages.error(request, "Please provide a valid GitHub repository URL")
            return redirect('assignment_detail', assignment_id=assignment_id)

        # Create or update submission
        submission, created = Submission.objects.update_or_create(
            assignment=assignment,
            student=request.user,
            defaults={
                'github_url': github_url,
                'status': 'submitted'
            }
        )

        # Call AI grading API (mock implementation)
        try:
            submission.ai_feedback = "Sample AI feedback\n\nCode quality: Good\nFunctionality: Excellent\nDocumentation: Needs improvement"
            submission.marks = 88.5
            submission.status = 'graded'
            submission.save()

            messages.success(request, "Assignment submitted and graded successfully!")
        except Exception as e:
            messages.warning(request, f"Assignment submitted but grading failed: {str(e)}")

        return redirect('assignment_detail', assignment_id=assignment_id)

    return redirect('dashboard')


@login_required
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submission = Submission.objects.filter(
        assignment=assignment,
        student=request.user
    ).first()

    if request.method == 'POST':
        github_url = request.POST.get('github_url')

        # Validate GitHub URL
        if not github_url or 'github.com' not in github_url:
            messages.error(request, "Please provide a valid GitHub repository URL")
            return redirect('assignment_detail', assignment_id=assignment_id)

        # Create or update submission
        submission, created = Submission.objects.update_or_create(
            assignment=assignment,
            student=request.user,
            defaults={
                'github_url': github_url,
                'status': 'submitted'
            }
        )

        # Call AI grading API (mock implementation - replace with real API call)
        try:
            # This would be your actual API call:
            # response = requests.post('https://your-ai-grader-api.com', json={'repo': github_url})
            # submission.ai_feedback = response.json().get('feedback')
            # submission.marks = response.json().get('score')

            # Mock response for demonstration:
            submission.ai_feedback = f"AI Feedback for {github_url}\n\nCode structure: Good\nError handling: Needs improvement\nDocumentation: Adequate"
            submission.marks = 85.5
            submission.status = 'graded'
            submission.save()

            messages.success(request, "Assignment submitted and graded successfully!")
        except Exception as e:
            messages.warning(request, f"Assignment submitted but grading failed: {str(e)}")

        return redirect('assignment_detail', assignment_id=assignment_id)

    # Faculty view logic
    if request.user.is_faculty:
        submissions = Submission.objects.filter(assignment=assignment)
        return render(request, 'faculty_assignment_detail.html', {
            'assignment': assignment,
            'submissions': submissions
        })

    # Student view
    return render(request, 'assignment_detail.html', {
        'assignment': assignment,
        'submission': submission
    })
from django.http import FileResponse

def download_assignment_pdf(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return FileResponse(assignment.pdf_file.open(), as_attachment=True)