# core/admin.py
from django.contrib import admin
from .models import User, Program, Class, Course, StudyMaterial, Assignment, Submission

admin.site.register(User)
admin.site.register(Program)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(StudyMaterial)
admin.site.register(Assignment)
admin.site.register(Submission)