from django.urls import path
from TaskHub.views import *


urlpatterns = [
    path('', login_page, name='login_page'),
    path('register/', register, name='register'),
    path('logout/',logout_page,name='logout_page'),

    path('dashboard/', home, name='home'),
    path('task_list/',task_list, name='task_list'),
    path('add_task/',add_task, name='add_task'),
    
    path('task_detail/<str:t_id>',task_detail, name='task_detail'),
    path('edit_task/<str:t_id>',edit_task, name='edit_task'),
    path('delete_task/<str:t_id>',delete_task, name='delete_task'),
]