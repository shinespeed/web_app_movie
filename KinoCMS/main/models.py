from django.db import models


class Post(models.Model):
    post_title = models.CharField('Name post', max_length=250)
    post_text = models.TextField('Text post')
    post_date_publish = models.DateTimeField('Date publish')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField('Name post', max_length=250)
    author_name = models.CharField('Name author', max_length=50)
    comment_date_publish = models.DateTimeField('Date publish')

