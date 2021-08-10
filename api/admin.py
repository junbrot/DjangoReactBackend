from django.contrib import admin
from .models import StudyBoard,Comment
from django.contrib.auth.models import User

# Register your models here.
@admin.register(StudyBoard)
class StudyBoardModel(admin.ModelAdmin):

    list_filter = ('StudyBoard_key','User_key','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')
    list_display = ('StudyBoard_key','User_key','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_filter = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')

# @admin.register(User)
# class UserModel(admin.ModelAdmin):
#     list_filter = ('id','username','password')
#     list_display = ('id', 'username', 'password')