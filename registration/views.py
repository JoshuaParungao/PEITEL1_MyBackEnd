from django.shortcuts import render

# Create your views here.
from .models import UserRegistration
from .serializer import UserRegistrationSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_user(request):
  serializer = UserRegistrationSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_user(request):

  users = UserRegistration.objects.all()
  serializer = UserRegistrationSerializer(users, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','PUT', 'DELETE'])
def user_detail(request, pk):
  try:
    user = UserRegistration.objects.get(pk=pk)
  except UserRegistration.DoesNotExist:
    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = UserRegistrationSerializer(user)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = UserRegistrationSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print("serializer errors:",serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
