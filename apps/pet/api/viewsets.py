from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.pet.models import Pet
from .serializers import PetSerializer
from project.infra.errors_message.unauthorized_signature import unauthorized_signature_message
from project.utils.user.is_authenticated import is_authenticated

class PetList(APIView): 
    def get(self, request, format=None):
        pet = Pet.objects.all()
        if is_authenticated(request):
            serializer = PetSerializer(pet, many=True)
            return Response(serializer.data)
        return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            if is_authenticated(request):
                serializer.save()
                return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
            return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PetDetail(APIView):
    def get_object(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pet = self.get_object(pk)
        if is_authenticated(request):   
            serializer = PetSerializer(pet)
            return Response(serializer.data)
        return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk, format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            if is_authenticated(request):
                return Response(serializer.data)
            return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pet = self.get_object(pk)
        if is_authenticated(request):
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(unauthorized_signature_message(), status=status.HTTP_403_FORBIDDEN)