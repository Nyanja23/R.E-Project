from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add-task/',views.add_task,name="add-task"),
    path('delete-task/<int:pk>/',views.delete_task,name="delete-task"),
    path('edit-task/<int:pk>/',views.edit_task,name="edit-task"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('register/',views.register,name="register"),
    path('edit-profile/', views.edit_profile_view, name='edit-profile'),
]