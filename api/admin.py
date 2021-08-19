from django.contrib import admin
from .models import StudyBoard,Comment,Applicant
from .models import Study,StudyMember,StudyPlanner,StudyPlannerComponent,StudyComment
from django.contrib.auth.models import User

# Register your models here.
@admin.register(StudyBoard)
class StudyBoardModel(admin.ModelAdmin):

    list_filter = ('StudyBoard_key','User_key','userId','title','lookupCount','uploadDate','duration')
    list_display = ('StudyBoard_key','User_key','userId','title','lookupCount','uploadDate','duration')

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_filter = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','StudyBoard_key','User_key','comment_date', 'comment_user', 'comment_textfield')

@admin.register(Applicant)
class ApplicantModel(admin.ModelAdmin):
    list_filter = ('id','StudyBoard_key','User_key','apply_user')
    list_display = ('id', 'StudyBoard_key', 'User_key', 'apply_user')

@admin.register(Study)
class StudyModel(admin.ModelAdmin):
    list_filter = ('id','User_key','StudyStartTime','duration')
    list_display = ('id', 'User_key', 'StudyStartTime','duration')

@admin.register(StudyMember)
class StudyMemberModel(admin.ModelAdmin):
    list_filter = ('id','Study_key','User_key')
    list_display = ('id', 'Study_key', 'User_key')

@admin.register(StudyPlanner)
class StudyPlannerModel(admin.ModelAdmin):
    list_filter = ('id','Study_key','User_key','title')
    list_display = ('id', 'Study_key', 'User_key','title')

@admin.register(StudyPlannerComponent)
class StudyPlannerComponentModel(admin.ModelAdmin):
    list_filter = ('id','Study_key','User_key','StudyPlanner_key','title','StudyPlannerComponentStartTime','duration')
    list_display = ('id', 'Study_key', 'User_key','title')

@admin.register(StudyComment)
class StudyCommentModel(admin.ModelAdmin):
    list_filter = ('id','Study_key','User_key','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','Study_key','User_key','comment_date', 'comment_user', 'comment_textfield')
