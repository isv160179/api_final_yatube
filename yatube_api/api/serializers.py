from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Comment, Group, Follow
from .fields import Base64ImageField

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    pub_date = serializers.DateTimeField(
        read_only=True,
        format="%d-%m-%Y %H:%M:%S"
    )
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    created = serializers.DateTimeField(
        read_only=True,
        format="%d-%m-%Y %H:%M:%S"
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже оформили подписку на этого пользователя!'
            ),
        )

    def validate_following(self, value):
        if value == self.context.get('request').user:
            raise serializers.ValidationError(
                'Нельзя оформить подписку на себя!'
            )
        return value
