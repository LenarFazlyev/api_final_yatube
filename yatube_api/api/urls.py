from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, PostViewSet, GroupViewSet, CommentViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentViewSet,
    basename='comments',
)
router_v1.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
    # path('v1/follow/', FollowViewSet.as_view()),
]
