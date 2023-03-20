from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "group", "pub_date")


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ("user", "following")
        read_only_fields = ("user",)

        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message=("Дубликат подписки"),
            ),
        )

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError(
                "Невозможно подписаться на себя."
            )
        return data
