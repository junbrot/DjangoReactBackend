from django.urls import path,include

from .views import StudyBoard_list,StudyBoard_detail,UserViewSet
from .views import Comments_list,Comments_detail,Comments_detail_byID
from .views import Applicant_list,Applicant_detail,Applicant_detail_byID
from .views import Study_list,Study_detail
from .views import StudyMember_list,StudyMember_detail,StudyMember_for_Key
from .views import StudyPlanner_list,StudyPlanner_detail,StudyPlanner_detail_byID
from .views import StudyPlannerComponent_list,StudyPlannerComponent_detail,StudyPlannerComponent_detail_byStudyPlannerID
from .views import StudyPlannerComponent_Maxdetail_byID
from .views import StudyComment_list,StudyComment_detail,StudyComment_detail_byID
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('StudyBoard',StudyBoardViewset,basename='StudyBoard')
# router.register('users',UserViewSet)
#
# User_list = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
# urlpatterns = router.urls


urlpatterns = [
    path('api/StudyBoard/',StudyBoard_list.as_view()),
    path('api/StudyBoard/<int:id>/',StudyBoard_detail.as_view()),
    path('api/Comments/',Comments_list.as_view()),
    path('api/Comments/<int:comment_pk>/', Comments_detail.as_view()),
    path('api/Comments/<int:comment_pk>/<int:id>/', Comments_detail_byID.as_view()),
    path('api/Applicants/',Applicant_list.as_view()),
    path('api/Applicants/<int:comment_pk>/', Applicant_detail.as_view()),
    path('api/Applicants/<int:comment_pk>/<int:id>/', Applicant_detail_byID.as_view()),
    path('api/Studys/',Study_list.as_view()),
    path('api/Studys/<int:id>/',Study_detail.as_view()),
    path('api/StudyMembers/',StudyMember_list.as_view()),
    path('api/StudyMembers/<int:id>/',StudyMember_detail.as_view()),
    path('api/StudyMemberForKey/<int:id>/',StudyMember_for_Key.as_view()),
    path('api/StudyPlanners/',StudyPlanner_list.as_view()),
    path('api/StudyPlanners/<int:id>/',StudyPlanner_detail.as_view()),
    path('api/StudyPlanners/<int:comment_pk>/<int:id>/',StudyPlanner_detail_byID.as_view()),
    path('api/StudyPlannerComponents/',StudyPlannerComponent_list.as_view()),
    path('api/StudyPlannerComponents/<int:id>/',StudyPlannerComponent_detail.as_view()),
    path('api/StudyPlannerComponents/<int:id2>/<int:id>/',StudyPlannerComponent_detail_byStudyPlannerID.as_view()),
    path('api/StudyPlannerComponents/<int:id3>/<int:id2>/<int:id>/',StudyPlannerComponent_Maxdetail_byID.as_view()),
    path('api/StudyComments/',StudyComment_list.as_view()),
    path('api/StudyComments/<int:id>/',StudyComment_detail.as_view()),
    path('api/StudyComments/<int:comment_pk>/<int:id>/',StudyComment_detail_byID.as_view()),
    path('api/',include(router.urls)),
    # path('api/users/',UserViewSet.as_view({'get'}),name='User_list'),
    # path('api/users/<int:id>/',UserViewSet.as_view({'retrieve'}),name='User_list'),
]
