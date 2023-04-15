from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape 
import markdown
from website.models import Post
register=template.Library()


@register.simple_tag
def total_posts():
	return Post.published.count()


@register.inclusion_tag('website/post/latest_posts.html')
def show_latest_posts(count=4):
	latest_posts=Post.published.order_by('-publish')[:count]
	return {'latest_posts':latest_posts}


@register.simple_tag
def get_most_commented_posts(count=4):
	comment=Post.published.annotate(total_comment=Count('comments'))

	return Post.published.annotate(total_comment=Count('comments')).exclude(total_comment=0).order_by('-total_comment')


@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))
