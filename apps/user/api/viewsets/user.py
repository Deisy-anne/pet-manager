from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from apps.user.models import User
from apps.user.api.serializers.user import UserSerializer
from project.utils.user.password_utils import validate_password
from project.utils.user.errors_message.password_is_invalid import invalid_password_message
from project.utils.user.is_authenticated import is_authenticated
from project.infra.errors_message.unauthorized_signature import unauthorized_signature_message

class UserList(APIView):
    def post(self, request, format=None):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
          if validate_password(serializer.initial_data['password']) == False:
              return Response(invalid_password_message(), status=status.HTTP_400_BAD_REQUEST)
          serializer.save()
          return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    def get_object(self, pk, format=None):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        if is_authenticated(request):
            return Response(serializer.data)
        return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            if is_authenticated(request):
                serializer.save()
                return Response(serializer.data)
            return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if is_authenticated(request):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
