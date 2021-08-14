from rest_framework import serializers
from .models import StudyBoard,Comment,Applicant,Study,StudyMember,StudyPlanner,StudyPlannerComponent
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class StudyBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyBoard
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = { 'password':{
            'write_only':True,
            'required':True
        }}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = '__all__'

class StudySerializer(serializers.ModelSerializer):

    class Meta:
        model = Study
        fields = '__all__'

class StudyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyMember
        fields = '__all__'

class StudyPlannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyPlanner
        fields = '__all__'


class StudyPlannerComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlannerComponent
        fields = '__all__'
