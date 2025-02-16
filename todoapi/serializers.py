from rest_framework import serializers
from .models import CustomUser, Task
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'phone_number', 'address', 'is_active', 'created_at', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        email = validated_data['email']
        first_name = validated_data['first_name']
        username = validated_data['username']
        last_name = validated_data['last_name']
        phone_number = validated_data['phone_number']
        address = validated_data['address']
        password = validated_data['password']

        user = get_user_model()
        new_user = user(email=email, username=username, phone_number=phone_number,
                        last_name=last_name, first_name=first_name, address=address)
        new_user.set_password(password)
        new_user.save()
        return new_user


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status',
                  'start_date', 'start_time', 'end_date', 'end_time']

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if end_date < start_date:
            raise serializers.ValidationError(
                {"end_date": "End date cannot be before start date."})

        # Ensure end_time is not before start_time if the task is on the same day
        if start_date == end_date and end_time < start_time:
            raise serializers.ValidationError(
                {"end_time": "End time cannot be before start time on the same day."})

        return data

    def create(self, validated_data):
        request = self.context.get('request')  # Get request context
        validated_data['user'] = request.user
        return Task.objects.create(**validated_data)


class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user', 'task_id', 'title', 'description', 'status',
                  'start_date', 'start_time', 'end_date', 'end_time']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Include user data
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "phone_number": self.user.phone_number,
            "address": self.user.address,
            "is_active": self.user.is_active,
        }

        return data
