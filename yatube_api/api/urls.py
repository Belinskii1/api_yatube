from django.urls import path, include
from .views import api_posts, api_posts_detail, GroupViewSet
from rest_framework.authtoken import views


app_name = 'api'

urlpatterns = [
    path('posts/', api_posts),
    path('posts/<int:pk>/', api_posts_detail),
    path('api-token-auth/', views.obtain_auth_token)
]

"""path('groups/', api_groups),"""
"""path('groups/<int:group_id>/', GroupViewSet.as_view()),"""