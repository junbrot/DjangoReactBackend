from .models import StudyBoard,Comment
from .serializers import StudyBoardSerializer,CommentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404


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


class Comments_list(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        comments = Comment.objects.all()
        serialized_comments = CommentSerializer(comments,many=True)
        return Response(serialized_comments.data)

    def post(self,request):
        serialized_Comment = CommentSerializer(data=request.data)
        if serialized_Comment.is_valid():
            serialized_Comment.save()
            return Response(serialized_Comment.data, status=status.HTTP_201_CREATED)
        return Response(serialized_Comment.errors, status=status.HTTP_400_BAD_REQUEST)


class Comments_detail(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request, comment_pk):

        Comments = Comment.objects.filter(StudyBoard_key=comment_pk)
        Serialized_Comments = CommentSerializer(Comments, many=True)
        return Response(Serialized_Comments.data)


class Comments_detail_byID(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request,comment_pk, id):
        try:
            one_Comment = Comment.objects.filter(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Serialized_one_Comment = CommentSerializer(one_Comment,many=True)
        return Response(Serialized_one_Comment.data)

    def put(self,request,comment_pk,id):

        one_Comment = get_object_or_404(Comment, id=id)
        serialized_one_Comment = CommentSerializer(one_Comment,data=request.data)
        if serialized_one_Comment.is_valid():
            serialized_one_Comment.save()
            return Response(serialized_one_Comment.data)
        return Response(serialized_one_Comment.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,comment_pk,id):

        one_Comment = get_object_or_404(Comment,id=id)
        one_Comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)