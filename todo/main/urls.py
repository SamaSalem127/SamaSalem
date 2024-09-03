from django.urls import path
from .views import index, detailed_subject, todo_by_status, todo_list_section, create_todo, create_section, update_subject, delete_subject, signup, login, logout, dashboard

urlpatterns = [
    path('', index, name='home'),
    path('detailed_subject/<int:id>/', detailed_subject, name='detailed_subject'),
    path('todo/update/<int:id>/', update_subject, name='update_subject'),
    path('todo/delete/<int:id>/', delete_subject, name='delete_subject'),
    path('todos/status/<str:st>/', todo_by_status, name='status'),
    path('todo/section/<int:id>/', todo_list_section, name='sectodo'),
    path('todo/create/', create_todo, name='createtodo'),
    path('section/create/', create_section, name='createsection'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
