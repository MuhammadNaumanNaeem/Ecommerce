from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User


def register_user(validated_data):
    try:
        password = validated_data.pop("password")
        validated_data["role"] = "user"

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)

        return {
            "success": True,
            "message": "User registered successfully.",
            "data": {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.role,
            },
            "status": 201,
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Internal Server Error",
            "error": str(e),
            "status": 500,
        }


def authenticate_user(email, password):
    try:
        user = authenticate(username=email, password=password)

        if not user:
            return {
                "success": False,
                "message": "Invalid email or password.",
                "status": 401,
            }

        refresh = RefreshToken.for_user(user)

        return {
            "success": True,
            "message": "Login successful.",
            "data": {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.role,
            },
            "status": 200,
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Internal Server Error",
            "error": str(e),
            "status": 500,
        }


def get_logged_in_user(user):
    try:
        return {
            "success": True,
            "message": "User profile fetched successfully.",
            "data": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            },
            "status": 200,
        }

    except Exception as e:
        return {
            "success": False,
            "message": "Internal Server Error",
            "error": str(e),
            "status": 500,
        }