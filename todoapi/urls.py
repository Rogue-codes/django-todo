from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_user_view),
    path('users/', views.UserListView.as_view(), name='users_list'),
    path('users/<int:pk>', views.UserDetailsView.as_view(), name='users_list'),
]

