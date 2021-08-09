from .models import StudyBoard,Comment
from .serializers import StudyBoardSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework import status

class StudyBoard_list(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        StudyBoards = StudyBoard.objects.all()
        serialized_StudyBoards = StudyBoardSerializer(StudyBoards,many=True)
        return Response(serialized_StudyBoards.data)

    def post(self,request):
        serialized_StudyBoards = StudyBoardSerializer(data=request.data)
        if serialized_StudyBoards.is_valid():
            serialized_StudyBoards.save()
            return Response(serialized_StudyBoards.data, status=status.HTTP_201_CREATED)
        return Response(serialized_StudyBoards.errors, status=status.HTTP_400_BAD_REQUEST)

class StudyBoard_detail(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_object(self,id):
        try:
            return StudyBoard.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        one_StudyBoard = self.get_object(id)
        # comments = Comment.objects.filter(id=id)
        serialized_one_StudyBoard = StudyBoardSerializer(one_StudyBoard)

        return Response(serialized_one_StudyBoard.data)

    def put(self,request,id):
        one_StudyBoard = self.get_object(id)
        serialized_one_StudyBoard = StudyBoardSerializer(one_StudyBoard,data=request.data)
        if serialized_one_StudyBoard.is_valid():
            serialized_one_StudyBoard.save()
            return Response(serialized_one_StudyBoard.data)
        return Response(serialized_one_StudyBoard.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        one_StudyBoard = self.get_object(id)
        one_StudyBoard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


# class StudyBoardViewset(viewsets.ModelViewSet):
#
#     queryset = StudyBoard.objects.all()
#     serializer_class = StudyBoardSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (TokenAuthentication,)
#
#
#
# class UserViewSet(viewsets.ModelViewSet):
#
#     serializer_class = UserSerializer
#     queryset = User.objects.all()



# from django.shortcuts import render,HttpResponse
# from .models import StudyBoard
# from .serializers import StudyBoardSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
#
# # Create your views here.
# from rest_framework.decorators import  APIView
# from rest_framework import generics
# from rest_framework import mixins
#
# from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
#
# class StudyBoardViewset(viewsets.ViewSet):
#
#     def list(self,request):
#         StudyBoards = StudyBoard.objects.all()
#         serializer = StudyBoardSerializer(StudyBoards,many=True)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer = StudyBoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request,pk=None):
#         queryset = StudyBoard.objects.all()
#         one_StudyBoard = get_object_or_404(queryset,pk=pk)
#         serializer = StudyBoardSerializer(one_StudyBoard)
#         return Response(serializer.data)
#
#     def update(self,request,pk=None):
#
#         one_StudyBoard = StudyBoard.objects.get(pk=pk)
#         serializer = StudyBoardSerializer(one_StudyBoard,data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request,pk=None):
#         one_StudyBoard = StudyBoard.objects.get(pk=pk)
#         one_StudyBoard.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class UserViewSet(viewsets.ModelViewSet):
#
#     serializer_class = UserSerializer
#     queryset = User.objects.all()