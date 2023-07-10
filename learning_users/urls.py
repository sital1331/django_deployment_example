from django.urls import path,include
from learning_users import views

app_name='learning_users'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login')
    
]