
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    # path('', views.index,name='index'),    
    path('', views.login_view, name='userlogin'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout, name='logout'),
    path('invest/', views.invest, name='invest'),
    path('project_details/', views.project_details, name='project_details'),


]
