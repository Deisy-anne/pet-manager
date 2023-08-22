from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

from apps.user.models import User
from apps.user.api.serializers.user_authentication import UserAuthenticationSerializer
from apps.user.api.errors_message.authentication_failed import authentication_failed_message
from project.infra.token import generate_token

class UserAuthenticationList(APIView):
    def post(self, request, format=None):
        serializer = UserAuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            existing_email = User.objects.filter(Q(email=serializer.initial_data['email']))
            valid_password = existing_email.filter(Q(password=serializer.initial_data['password']))
            if len(existing_email) == 0 or len(valid_password) == 0:
                return Response(authentication_failed_message(), status=status.HTTP_401_UNAUTHORIZED)
            token = generate_token(serializer.data['email'])
            return Response(token)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
