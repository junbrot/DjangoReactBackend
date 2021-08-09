from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudyBoard(models.Model):

    # userkey = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    userId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='')
    userBigCity = models.CharField(max_length=10)
    userSmallCity = models.CharField(max_length=10)
    userDetailCity = models.CharField(max_length=100)
    gatherMember = models.IntegerField(default=4)
    lookupCount = models.IntegerField(default=0)
    uploadDate = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.id

class Comment(models.Model) :

    studyboard = models.ForeignKey(StudyBoard,on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_textfield = models.TextField()
