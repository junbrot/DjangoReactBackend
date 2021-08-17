from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

class StudyBoard(models.Model):

    User_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    StudyBoard_key = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='')
    gatherMember = models.IntegerField(default=4)
    ApplyMember = models.IntegerField(default=1)
    lookupCount = models.IntegerField(default=0)
    uploadDate = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(validators=[MinValueValidator(29),MaxValueValidator(91)],default=30)

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
    title = models.CharField(max_length=50, default='')
    StudyStartTime = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(validators=[MinValueValidator(29),MaxValueValidator(91)],default=30)

class StudyMember(models.Model):

    Study_key = models.ForeignKey(Study,on_delete=models.CASCADE,null=True)
    User_key = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class StudyPlanner(models.Model):

    Study_key = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)
    User_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userId = models.CharField(max_length=20,default='')
    title = models.CharField(max_length=50, default='')

class StudyPlannerComponent(models.Model):

    Study_key = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)
    User_key = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userId = models.CharField(max_length=20, default='')
    StudyPlanner_key = models.ForeignKey(StudyPlanner, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, default='')
    StudyPlannerComponentStartTime = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=30)
    condition = models.IntegerField(default=0)
