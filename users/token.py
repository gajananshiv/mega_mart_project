# users/token.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

'''class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims if needed
        token['email'] = user.email
        return token

    def validate(self, attrs):
        # Accept "email" instead of "username"
        credentials = {
            'email': attrs.get("email"),
            'password': attrs.get("password"),
        }

        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=credentials['email'])
        except user_model.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        if not user.check_password(credentials['password']):
            raise serializers.ValidationError("Incorrect password")

        data = super().validate({
            'username': user.email,
            'password': credentials['password']
        })

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
'''