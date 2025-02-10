import django_filters
from .models import CustomUser, Task
class UserFilter(django_filters.FilterSet):
    class Meta:
        model=CustomUser
        fields={
            'username':['exact', 'icontains']
        }
        
class TaskFilter(django_filters.FilterSet):
    class Meta:
        model=Task
        fields={
            'title':['exact', 'icontains']
        }