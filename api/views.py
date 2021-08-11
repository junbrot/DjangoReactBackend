from .models import StudyBoard,Comment,Applicant
from .serializers import StudyBoardSerializer,CommentSerializer,ApplicantSerializer
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
            return StudyBoard.objects.get(StudyBoard_key=id)
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

class Applicant_list(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        applicants = Applicant.objects.all()
        serialized_applicants = ApplicantSerializer(applicants, many=True)
        return Response(serialized_applicants.data)

    def post(self, request):
        serialized_applicants = ApplicantSerializer(data=request.data)
        if serialized_applicants.is_valid():
            serialized_applicants.save()
            return Response(serialized_applicants.data, status=status.HTTP_201_CREATED)
        return Response(serialized_applicants.errors, status=status.HTTP_400_BAD_REQUEST)

class Applicant_detail(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request, comment_pk):

        applicants = Applicant.objects.filter(StudyBoard_key=comment_pk)
        serialized_applicants = ApplicantSerializer(applicants, many=True)
        return Response(serialized_applicants.data)

    def post(self, request,comment_pk):
        serialized_applicants = ApplicantSerializer(data=request.data)
        if serialized_applicants.is_valid():
            serialized_applicants.save()
            return Response(serialized_applicants.data, status=status.HTTP_201_CREATED)
        return Response(serialized_applicants.errors, status=status.HTTP_400_BAD_REQUEST)


class Applicant_detail_byID(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request,comment_pk, id):
        try:
            one_applicant = Applicant.objects.filter(User_key=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_one_applicant = ApplicantSerializer(one_applicant,many=True)
        return Response(serialized_one_applicant.data)

    def put(self,request,comment_pk,id):

        one_applicant = get_object_or_404(Applicant, User_key=id)
        serialized_one_applicant = ApplicantSerializer(one_applicant,data=request.data)
        if serialized_one_applicant.is_valid():
            serialized_one_applicant.save()
            return Response(serialized_one_applicant.data)
        return Response(serialized_one_applicant.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,comment_pk,id):

        one_applicant = get_object_or_404(Applicant,User_key=id)
        one_applicant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)