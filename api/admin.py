from django.contrib import admin
from .models import StudyBoard,Comment

# Register your models here.
@admin.register(StudyBoard)
class StudyBoardModel(admin.ModelAdmin):

    list_filter = ('StudyBoard_key','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')
    list_display = ('StudyBoard_key','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_filter = ('id','StudyBoard_key','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','StudyBoard_key','comment_date', 'comment_user', 'comment_textfield')