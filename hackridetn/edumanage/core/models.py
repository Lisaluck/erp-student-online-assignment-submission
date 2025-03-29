from django.db import models
from django.contrib.auth.models import AbstractUser


class Program(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Class(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    year = models.IntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.program.name} Year {self.year} Section {self.section}"


class User(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=False)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    department = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def get_program(self):
        """Safe way to get program through student_class"""
        return self.student_class.program if self.student_class else None

    def get_year(self):
        """Safe way to get year through student_class"""
        return self.student_class.year if self.student_class else None

    def get_section(self):
        """Safe way to get section through student_class"""
        return self.student_class.section if self.student_class else None
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    class_associated = models.ForeignKey(Class, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_classes = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.class_associated}"


class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='study_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    max_marks = models.IntegerField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    github_repo = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    ai_feedback = models.TextField(blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"



