from django.contrib import admin
from .models import StudyBoard,Comment,Applicant,Study,StudyMember
from django.contrib.auth.models import User

# Register your models here.
@admin.register(StudyBoard)
class StudyBoardModel(admin.ModelAdmin):

    list_filter = ('StudyBoard_key','User_key','userId','title','lookupCount','uploadDate')
    list_display = ('StudyBoard_key','User_key','userId','title','lookupCount','uploadDate')

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_filter = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')

@admin.register(Applicant)
class ApplicantModel(admin.ModelAdmin):
    lint_filter = ('id','StudyBoard_key','User_key','apply_user','apply_textfield')

@admin.register(Study)
class StudyModel(admin.ModelAdmin):
    lint_filter = ('id','User_key')

@admin.register(StudyMember)
class StudyMemberModel(admin.ModelAdmin):
    lint_filter = ('id','Study_key','User_key')
