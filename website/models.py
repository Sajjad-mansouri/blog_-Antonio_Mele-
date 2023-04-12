from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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


	class Meta:
		ordering=['-publish']
	def __str__(self):
		return self.title