from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_user_view),
    path('users/', views.UserListView.as_view(), name='users_list'),
    path('users/<int:pk>', views.UserDetailsView.as_view(), name='user'),
    path('task/create/', views.CreateTaskApiview.as_view()),
    path('tasks/all/', views.MyTaskListApiView.as_view(), name='tasks_list'),
    path('tasks/<uuid:task_id>', views.TaskDetailsView.as_view(), name='task'),
    path("tasks/<uuid:task_id>/status/",
         views.UpdateTaskStatusView.as_view(), name="update_task_status"),

]
