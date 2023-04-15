from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .models import Post


class PostFeed(Feed):
	title='blog website Feed'
	link='/website/'
	description='this is blog website feed'

	def items(self):
		return Post.published.order_by('-publish')[:5]

	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return truncatewords(item.description,30)