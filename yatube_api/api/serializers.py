from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post
from posts.models import Group
from posts.models import Comment
from posts.models import Follow
from posts.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following',)
        model = Follow

    def validate_following(self, data):
        if data == self.context['request'].user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя")
        return data

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
        )
    ]
