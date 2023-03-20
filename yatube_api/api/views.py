from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from django.shortcuts import get_object_or_404

from posts.models import Follow, Group, Post

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""

    queryset = Post.objects.select_related("author")
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.select_related("author")

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        serializer.save(
            author=self.request.user, post=get_object_or_404(Post, pk=post_id)
        )


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для подписок."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "following__username",
        "user__username",
    )

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
