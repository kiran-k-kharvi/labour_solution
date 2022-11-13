from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from lb_sol.helpers.helpers import get_tokens_for_user
from user_auth.serializers.serializers import UserLoginSerializer


class UserLogin(APIView):
    def post(self, request, format=None):
        _serializer = UserLoginSerializer(data=request.data)
        if _serializer.is_valid():
            data = _serializer.data
            email = data.get('email')
            password = data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response({"token": token}, status=HTTP_200_OK)
            else:
                return Response({"error": {'non_field_error': 'email or password is invalid'}},
                                status=HTTP_400_BAD_REQUEST)
        return Response(_serializer.errors, status=HTTP_400_BAD_REQUEST)
