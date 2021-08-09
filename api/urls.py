from django.urls import path,include
from .views import StudyBoard_list,StudyBoard_detail,UserViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('StudyBoard',StudyBoardViewset,basename='StudyBoard')
# router.register('users',UserViewSet)

urlpatterns = [
    path('api/StudyBoard/',StudyBoard_list.as_view()),
    path('api/StudyBoard/<int:id>/',StudyBoard_detail.as_view()),
    # path('api/StudyBoard/userkey/<int:id>',StudyBoard_detail.as_view()),
    path('api/users/',UserViewSet)
]
