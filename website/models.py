from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManger(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='p')

class Post(models.Model):
	STATUS_CHOICE=(
		('d','draft'),
		('p','publish'))
	title=models.CharField(max_length=50)
	slug=models.SlugField(max_length=50,unique_for_date='publish')
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	description=models.TextField()
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	status=models.CharField(max_length=1,choices=STATUS_CHOICE)
	tags = TaggableManager()

	objects=models.Manager()
	published=PublishedManger()

	class Meta:
		ordering=['-publish']
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('website:detail',kwargs={'slug':self.slug,
										'year':self.publish.year,
										'month':self.publish.month,
										'day':self.publish.day})

class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	body=models.TextField()
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	class Meta:
		ordering=['-created']

	def __str__(self):
		return f'comment {self.name} for post:{self.post}'
