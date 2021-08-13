from django.db import models
from django.contrib.auth.models import User

class StudyBoard(models.Model):

    User_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    StudyBoard_key = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='')
    # userBigCity = models.CharField(max_length=10)
    # userSmallCity = models.CharField(max_length=10)
    # userDetailCity = models.CharField(max_length=100)
    gatherMember = models.IntegerField(default=4)
    ApplyMember = models.IntegerField(default=1)
    lookupCount = models.IntegerField(default=0)
    uploadDate = models.DateTimeField(auto_now_add=True)


class Comment(models.Model) :

    StudyBoard_key = models.ForeignKey(StudyBoard,on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.CharField(max_length=20)
    comment_textfield = models.CharField(max_length=200)
    User_key = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


class Applicant(models.Model):

    StudyBoard_key = models.ForeignKey(StudyBoard,on_delete=models.CASCADE, null=True)
    apply_user = models.CharField(max_length=20)
    User_key = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

class Study(models.Model):

    User_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # title = models.CharField(max_length=50)

class StudyMember(models.Model):

    Study_key = models.ForeignKey(Study,on_delete=models.CASCADE,null=True)
    User_key = models.OneToOneField(User, on_delete=models.CASCADE, null=True)