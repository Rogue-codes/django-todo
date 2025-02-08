from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, filters
from .models import CustomUser
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

@api_view(['POST'])
def create_user_view(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    
