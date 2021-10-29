from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.db import IntegrityError


class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
     
        user = authenticate(username=username, password=password)
        if user != None:         
            token = Token.objects.get_or_create(user=user)[0]

            return Response({'token': token.key})

        else:
            return Response({"error": "Worng username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        

class AccountsView(APIView):
    def post(self, request):
        
        try:
            new_user =  User.objects.create_user(
                username = request.data["username"],
                password = request.data["password"],
                is_superuser = request.data["is_superuser"],
                is_staff = request.data["is_staff"]
            )
        except IntegrityError:
            return Response({"user already exists"},status=status.HTTP_409_CONFLICT)

        print(">>>>>>>>>>>", new_user)

        return Response("", status=status.HTTP_201_CREATED)




