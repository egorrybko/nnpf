# thumbnailer/urls.py
from django.urls import path
from django.urls import include, re_path
from . import views
from .views import e_handler404, e_handler500
 
urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('main', views.main, name='main'),
  path('about_prj', views.about_prj, name='about_prj'),
  path('about_us', views.about_us, name='about_us'),
  path('task/<str:task_id>/', views.TaskView.as_view(), name='task'),
  path('test', views.test, name='test'),
  path('signup/',views.sign_up, name='signup'),
  path('login/',views.user_login, name='login'),
  path('profile/',views.user_profile,name='profile'),
  path('logout/',views.user_logout,name='logout'),
]

handler404 = e_handler404
handler500 = e_handler500