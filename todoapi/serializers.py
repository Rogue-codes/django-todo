from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'phone_number', 'address', 'is_active', 'created_at']
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
