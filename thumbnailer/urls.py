# thumbnailer/urls.py
from django.urls import path
from . import views
urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('main', views.main, name='main'),
  path('about_prj', views.about_prj, name='about_prj'),
  path('about_us', views.about_us, name='about_us'),
  path('task/<str:task_id>/', views.TaskView.as_view(), name='task'),
]