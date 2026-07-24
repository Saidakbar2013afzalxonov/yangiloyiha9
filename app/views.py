from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, RefreshSerializer
from rest_framework import generics, status


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "passport_number": request.user.passport_number,
            "phone": request.user.phone,
            "profession": request.user.profession,
            "salary": request.user.salary,
            "is_verified": request.user.is_verified,
            "slug": request.user.slug,
            "created_at": request.user.created_at,
        })


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout successful."})

        except Exception:
            return Response(
                {"error": "Invalid refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        return Response(serializer.validated_data, status = status.HTTP_200_OK)


class RefreshAPIView(APIView):
    def post(self, request):
        serializer = RefreshSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)