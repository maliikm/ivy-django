from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:primary_key>/<int:age>', views.project, name="project")
]