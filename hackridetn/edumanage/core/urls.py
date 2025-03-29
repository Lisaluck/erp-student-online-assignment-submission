from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import profile_view

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard/')),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/add-material/', views.add_study_material, name='add_study_material'),
    path('course/<int:course_id>/create-assignment/', views.create_assignment, name='create_assignment'),
    path('profile/', profile_view, name='profile'),
    path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('assignments/<int:assignment_id>/pdf/', views.download_assignment_pdf, name='download_assignment_pdf'),
]