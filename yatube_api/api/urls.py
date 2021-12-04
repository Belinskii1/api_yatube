from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('groups', GroupViewSet)
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')


app_name = 'api'

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]

"""path('groups/', api_groups),"""
"""path('groups/<int:group_id>/', GroupViewSet.as_view()),"""