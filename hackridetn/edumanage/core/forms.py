from django import forms
from .models import Course, StudyMaterial, Assignment, Submission, User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_faculty', 'is_student']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'title', 'class_associated', 'start_date', 'end_date', 'total_classes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['title', 'description', 'file']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'max_marks']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['github_repo']


from django import forms
from .models import User, Program,Class

from django import forms
from .models import User, Program, Class


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.is_student:
            self.fields['student_class'] = forms.ModelChoiceField(
                queryset=Class.objects.all().order_by('program__name', 'year', 'section'),
                required=True,
                initial=self.instance.student_class,
                label="Your Class"
            )
        elif self.instance.is_faculty:
            self.fields['department'] = forms.CharField(
                required=True,
                initial=self.instance.department
            )
            self.fields['designation'] = forms.CharField(
                required=True,
                initial=self.instance.designation
            )

    def save(self, commit=True):
        user = super().save(commit=False)

        if user.is_student:
            user.student_class = self.cleaned_data.get('student_class')
        elif user.is_faculty:
            user.department = self.cleaned_data.get('department')
            user.designation = self.cleaned_data.get('designation')

        if commit:
            user.save()
        return user