from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import RegisterSerializer
from .services import register_user, authenticate_user, get_logged_in_user

from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    @extend_schema(
    summary="Register User",
    description="Register a new user account.",
    request=RegisterSerializer,
    responses={201: RegisterSerializer},
    )

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)

            if serializer.is_valid():
                response = register_user(serializer.validated_data)
            else:
                response = {
                    "success": False,
                    "message": "Validation Error",
                    "errors": serializer.errors,
                    "status": 400,
                }

            return Response(
                {
                    "success": response["success"],
                    "message": response["message"],
                    **({"data": response["data"]} if "data" in response else {}),
                    **({"errors": response["errors"]} if "errors" in response else {}),
                    **({"error": response["error"]} if "error" in response else {}),
                },
                status=response["status"],
            )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    @extend_schema(
    summary="Login User",
    description="Authenticate user and return JWT access and refresh tokens.",
    request=LoginSerializer,
    )
    
    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            if not email or not password:
                return Response(
                    {
                        "success": False,
                        "message": "Email and password are required.",
                    },
                    status=400,
                )

            response = authenticate_user(email, password)

            return Response(
                {
                    "success": response["success"],
                    "message": response["message"],
                    **({"data": response["data"]} if "data" in response else {}),
                    **({"error": response["error"]} if "error" in response else {}),
                },
                status=response["status"],
            )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
    summary="Current User",
    description="Retrieve the authenticated user's profile."
    )

    def get(self, request):
        try:
            response = get_logged_in_user(request.user)

            return Response(
                {
                    "success": response["success"],
                    "message": response["message"],
                    "data": response["data"],
                },
                status=response["status"],
            )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )