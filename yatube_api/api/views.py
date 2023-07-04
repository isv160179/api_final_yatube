from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .mixins import PermissionForRetrieveMixin
from .permissions import (
    IsAuthorPostOrReadOnly,
    IsAuthorCommentOrReadOnly
)
from .serializers import (
    GroupSerializer,
    FollowSerializer,
    PostSerializer,
    CommentSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(PermissionForRetrieveMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorPostOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(PermissionForRetrieveMixin):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorCommentOrReadOnly,)

    def __get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.__get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.__get_post())


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
