from django.shortcuts import get_object_or_404
from rest_framework import viewsets, pagination, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter


from .serializers import (FollowSerializer, CommentSerializer,
                          GroupSerializer, PostSerializer)
from .permissions import OwnerOrReadOnly
from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnerOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    permission_classes = [OwnerOrReadOnly]

    def post_get(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.post_get().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.post_get())

# Оставил чтобы показать другой способ.
# При таком способе необходимо менять url
# Удалю потом
# class FollowViewSet(generics.ListCreateAPIView):
#     queryset = Follow.objects.all()
#     serializer_class = FollowSerializer

#     def get_queryset(self):
#         return self.request.user.follower.all()

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        following = serializer.validated_data['following']
        if following == self.request.user:
            raise ValidationError("Нельзя подписаться на самого себя")
        serializer.save(user=self.request.user)
