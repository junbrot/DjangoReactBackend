from django.contrib import admin
from .models import StudyBoard,Comment

# Register your models here.
@admin.register(StudyBoard)
class StudyBoardModel(admin.ModelAdmin):

    list_filter = ('id','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')
    list_display = ('id','userId','title','userBigCity','userSmallCity','userDetailCity','lookupCount','uploadDate')

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_filter = ('id','studyboard','comment_date', 'comment_user', 'comment_textfield')
    list_display = ('id','studyboard','comment_date', 'comment_user', 'comment_textfield')