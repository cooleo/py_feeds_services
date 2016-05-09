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
    tags = TagSerializer(many=True, read_only=False)
    photo = PhotoSerializer(required=False, read_only=False)
    video = VideoSerializer(required=False, read_only=False)
    news = NewsSerializer(required=False, read_only=False)
    images = PhotoSerializer(many=True, read_only=False)
    category = CategorySerializer(required=False, read_only=False)

    class Meta:
        model = Feed
        fields = (
            'title', 'description', 'bucket', 'thumb', 'url', 'content', 'likes', 'shares', 'pins', 'comments', 'views',
            'popular', 'tags', 'category', 'from_source', 'logo_source', 'name_source', 'createdAt', 'updatedAt',
            'type', 'status', 'video', 'images', 'photo', 'news')

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)

        photo_data = validated_data.pop('photo')
        video_data = validated_data.pop('video')
        news_data = validated_data.pop('news')
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        tags_data = validated_data.pop('tags')
        if photo_data is not None:
            photo = Photo.objects.create(**photo_data)
        if video_data is not None:
            video = Video.objects.create(**video_data)
        if news_data is not None:
            news = News.objects.create(**news_data)
        if category_data is not None:
            category = Category.objects.create(**category_data)
        if images_data is not None:
            images = Photo.objects.create(*images_data)
        if tags_data is not None:
            tags = Tag.objects.create(*tags_data)

        feed = Feed.objects.create(photo=photo, video=video, news=news, category=category, images=images, tags=tags,
                                   **validated_data)

        return feed


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    to = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='to'
    )

    class Meta:
        model = Notification
        fields = ('message', 'activity', 'to', 'status', 'createdAt', 'updatedAt')
