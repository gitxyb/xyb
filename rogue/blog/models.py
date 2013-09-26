#coding:utf8
from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
	user     = models.OneToOneField(User,related_name='u')
	birthday = models.DateField()
	sex      = models.CharField(max_length=10,choices=(('male','男'),('famle','女')))
	headImg  = models.FileField(upload_to="./headImg/")

	def __unicode__(self):
		return self.user.username

class Post(models.Model):
	user = models.ForeignKey(User)

	title = models.CharField(max_length=50)
	content = models.TextField()
	img = models.FileField(upload_to="./Img/")
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Replay(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	content = models.TextField()
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content

