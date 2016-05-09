from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    slug = models.CharField(max_length=1024)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class User(models.Model):
    email = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Tag(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Input(models.Model):
    logo = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=1024)
    channel_id = models.CharField(max_length=100)
    olikes = models.BigIntegerField
    ofollows = models.BigIntegerField
    osubcribles = models.BigIntegerField
    likes = models.BigIntegerField
    follows = models.BigIntegerField
    subribles = models.BigIntegerField
    tags = models.ForeignKey(Tag)
    categories = models.ForeignKey(Category)
    from_source = models.CharField(max_length=256)
    logo_source = models.CharField(max_length=256)
    name_source = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Video(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    bucket = models.CharField(max_length=256)
    filename = models.CharField(max_length=256)
    embed = models.CharField(max_length=256)
    source_id = models.CharField(max_length=256)
    duration = models.CharField(max_length=256)
    length = models.CharField(max_length=256)
    thumb = models.CharField(max_length=256)
    type = models.IntegerField
    from_source = models.CharField(max_length=256)
    logo_source = models.CharField(max_length=256)
    name_source = models.CharField(max_length=256)
    ext = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Photo(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    width = models.IntegerField
    height = models.IntegerField
    bucket = models.CharField(max_length=256)
    filename = models.CharField(max_length=256)
    version = models.CharField(max_length=256)
    path = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    ext = models.CharField(max_length=5)
    type = models.IntegerField
    from_source = models.CharField(max_length=256)
    logo_source = models.CharField(max_length=256)
    name_source = models.CharField(max_length=256)
    url_source = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class News(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    summary = models.CharField(max_length=1024)
    url = models.CharField(max_length=256)
    body = models.CharField(max_length=1024)
    thumb = models.CharField(max_length=256)
    bucket = models.CharField(max_length=256)
    photos = models.ForeignKey(Photo)
    author = models.OneToOneField(User)
    from_source = models.CharField(max_length=256)
    logo_source = models.CharField(max_length=256)
    name_source = models.CharField(max_length=256)
    url_source = models.CharField(max_length=256)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Feed(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    url = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)
    from_source = models.CharField(max_length=256)
    logo_source = models.CharField(max_length=256)
    name_source = models.CharField(max_length=256)
    url_source = models.CharField(max_length=256)
    type = models.IntegerField
    owner = models.ForeignKey(User)
    bucket = models.CharField(max_length=256)
    thumb = models.CharField(max_length=1024)
    likes = models.BigIntegerField
    shares = models.BigIntegerField
    pins = models.BigIntegerField
    comments = models.BigIntegerField
    pints = models.BigIntegerField
    views = models.BigIntegerField
    popular = models.BigIntegerField
    tags = models.ForeignKey(Tag)
    status = models.IntegerField
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    images = models.ForeignKey(Photo, related_name='images')
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE)
    news = models.OneToOneField(News, on_delete=models.CASCADE)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Activity(models.Model):
    user = models.ForeignKey(User, related_name='user')
    following = models.ForeignKey(User, related_name='following')
    feed = models.ForeignKey(Feed)
    action = models.CharField(max_length=1024)
    action_type = models.IntegerField
    content = models.CharField(max_length=1024)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Comment(models.Model):
    feed = models.ForeignKey(Feed)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=1024)
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField


class Notification(models.Model):
    message = models.CharField(max_length=1024)
    activity = models.ForeignKey(Activity)
    to = models.ForeignKey(User)
    status = models.IntegerField
    createdAt = models.DateTimeField
    updatedAt = models.DateTimeField
