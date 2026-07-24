from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "email", "password", "passport_number", "phone", "profession", "salary", "is_verified", "slug", "created_at"]
        read_only_fields = ["id", "slug", "created_at", "is_verified"]

    def create(self, validated_data):
        user = CustomUser()
        user.username = validated_data.get("username")
        user.first_name = validated_data.get("first_name")
        user.last_name = validated_data.get("last_name")
        user.email = validated_data.get("email")
        user.passport_number = validated_data.get("passport_number")
        user.phone = validated_data.get("phone")
        user.profession = validated_data.get("profession")
        user.salary = validated_data.get("salary")
        user.set_password(validated_data.get("password"))
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username = username, password= password)

        if user is None:
            raise serializers.ValidationError("xatolik bor")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }


class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get("refresh")

        try:
            token = RefreshToken(RefreshToken)
            return {
                "access":str(token.access_token)
            }

        except TokenError:
            raise serializers.ValidationError("xatolik bor")