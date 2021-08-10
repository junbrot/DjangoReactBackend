from rest_framework import serializers
from .models import StudyBoard,Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class StudyBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyBoard
        fields = ['StudyBoard_key','userId','title','description','userBigCity','userSmallCity',
                  'userDetailCity','gatherMember']

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

    # def get_comments(self,obj):
    #     comment_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    #     model= Comment
    #     fields = '__all__'