from django.urls import path,include
from .views import StudyBoard_list,StudyBoard_detail,UserViewSet,UserViewSet_detail
from .views import Comments_detail,Comments_list,Comments_detail_byUser,getCurrentUserId
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
    path('api/Comments/<int:comment_pk>/<int:user_pk>/', Comments_detail_byUser.as_view()),
    path('api/users/',User_list,name='User_list'),
    path('api/users/<int:comment_pk>',UserViewSet_detail.as_view()),
    path('api/test/',getCurrentUserId.as_view())
]
