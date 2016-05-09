from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import Category, Activity, Comment, News, Feed, Photo, Video, User, Notification, Tag, Input


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'slug')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    feed = serializers.StringRelatedField(many=False)

    class Meta:
        model = Activity
        fields = ('user', 'following', 'feed', 'action', 'action_type', 'content', 'createdAt', 'updatedAt')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    feed = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Comment
        fields = ('user', 'feed', 'content', 'createdAt', 'updatedAt')


# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     to = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Comment
#         fields = ('message', 'activity', 'to', 'status', 'createdAt', 'updatedAt')


class InputSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Input
        fields = (
            'logo', 'name', 'url', 'channel_id', 'olikes', 'ofollows', 'osubcribles', 'likes', 'follows', 'subribles',
            'tags', 'categories', 'from_source', 'logo_source', 'name_source', 'createdAt', 'updatedAt')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'slug', 'createdAt', 'updatedAt')


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = (
            'title', 'description', 'bucket', 'filename', 'embed', 'source_id', 'duration', 'length', 'thumb', 'type',
            'from_source', 'logo_source', 'name_source', 'createdAt', 'updatedAt', 'ext')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'width', 'height', 'bucket', 'filename', 'version', 'path', 'url', 'type',
                  'from_source', 'logo_source', 'name_source', 'createdAt', 'updatedAt', 'ext')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.StringRelatedField(many=True)

    class Meta:
        model = News
        fields = (
            'title', 'description', 'summary', 'body', 'bucket', 'thumb', 'photos', 'author', 'url', 'type',
            'from_source',
            'logo_source', 'name_source', 'createdAt', 'updatedAt')


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='photo'
    )
    video = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='video'
    )
    news = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='news'
    )
    tags = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tags'
    )
    category = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='category'
    )

    class Meta:
        model = Feed
        fields = (
            'title', 'description', 'bucket', 'thumb', 'url', 'content', 'likes', 'shares', 'pins', 'comments', 'views',
            'popular', 'tags', 'category', 'from_source', 'logo_source', 'name_source', 'createdAt', 'updatedAt',
            'type', 'status', 'video', 'images', 'photo', 'news')


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    to = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='to'
    )

    class Meta:
        model = Notification
        fields = ('message', 'activity', 'to', 'status', 'createdAt', 'updatedAt')
