from django.shortcuts import render
from .serializers import CustomUserSerializer, CreateTaskSerializer, GetTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Task
from .filters import UserFilter, TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

@api_view(['POST'])
def create_user_view(request):
    serializer = CustomUserSerializer(data=request.data)
    message = "Account created successfully"
    if serializer.is_valid():
        serializer.save()
        return Response({"message": message, "data": serializer.data, }, status=status.HTTP_201_CREATED)
    return Response({"message": "Account creation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_class = UserFilter
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username']


class UserDetailsView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# class CreateTaskApiview(generics.CreateAPIView):
#     model = Task
#     serializer_class = CreateTaskSerializer
#     permission_classes = [IsAuthenticated]

#     def get_serializer_context(self):
#         return {"request": self.request}

class CreateTaskApiview(generics.CreateAPIView):
    model = Task
    serializer_class = CreateTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Task created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class TaskListApiview(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = GetTaskSerializer
    filterset_class = TaskFilter
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title']
    
class MyTaskListApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = GetTaskSerializer
    filterset_class = TaskFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailsView (generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = GetTaskSerializer
    lookup_field = 'task_id'

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer