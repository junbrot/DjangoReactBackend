from django.urls import path,include
from .views import StudyBoard_list,StudyBoard_detail,UserViewSet
from .views import Comments_list,Comments_detail,Comments_detail_byID
from .views import Applicant_list,Applicant_detail,Applicant_detail_byID
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('StudyBoard',StudyBoardViewset,basename='StudyBoard')
# router.register('users',UserViewSet)

User_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api/StudyBoard/',StudyBoard_list.as_view()),
    path('api/StudyBoard/<int:id>/',StudyBoard_detail.as_view()),
    path('api/Comments/',Comments_list.as_view()),
    path('api/Comments/<int:comment_pk>/', Comments_detail.as_view()),
    path('api/Comments/<int:comment_pk>/<int:id>/', Comments_detail_byID.as_view()),
    path('api/Applicants/',Applicant_list.as_view()),
    path('api/Applicants/<int:comment_pk>/', Applicant_detail.as_view()),
    path('api/Applicants/<int:comment_pk>/<int:id>/', Applicant_detail_byID.as_view()),
    path('api/users/',User_list,name='User_list'),
]
