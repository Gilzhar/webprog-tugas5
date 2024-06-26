from django.urls import path
from myFirstapp import views

app_name = 'myFirstapp'
urlpattern = [
    path('', views.readStudent, name='read-data-student'),
    path('create/', views.readStudent, name='create-data-student'),
    path('update/', views.readStudent, name='update-data-student'),
     path('delete/', views.readStudent, name='delete-data-student'),
]