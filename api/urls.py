from django.urls import path,include
from .views import StudyBoard_list,StudyBoard_detail,UserViewSet
from .views import Comments_detail,Comments_list
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('StudyBoard',StudyBoardViewset,basename='StudyBoard')
# router.register('users',UserViewSet)

urlpatterns = [
    path('api/StudyBoard/',StudyBoard_list.as_view()),
    path('api/StudyBoard/<int:id>/',StudyBoard_detail.as_view()),
    path('api/Comments/',Comments_list.as_view()),
    path('api/Comments/<int:comment_pk>/', Comments_detail.as_view()),
    path('api/users/',UserViewSet),
]
