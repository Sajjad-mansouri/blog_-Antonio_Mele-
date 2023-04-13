from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail
from taggit.models import Tag
from . import forms
from .models import Post


class PostList(ListView):
	queryset=Post.published.all()
	template_name='website/post/list.html'
	paginate_by=1
	context_object_name='posts'

def post_list(request,tag_name=None):

	posts=Post.published.all()
	tag=None
	if tag_name:
		tag=get_object_or_404(Tag,slug=tag_name)
		posts=posts.filter(tags__in=[tag])
	paginator=Paginator(posts,1)
	page_number=request.GET.get('page')
	page_object=paginator.get_page(page_number)
	return render(request,'website/post/list.html',context={'posts':page_object,'tag':tag})


def post_detail(request,**kwargs):
	print(kwargs['slug'])

	post=get_object_or_404(Post,slug=kwargs['slug'],
								status='p',
								publish__year=kwargs['year'],
								publish__month=kwargs['month'],
								publish__day=kwargs['day'],
								

												)

	# return render(request,'website/post/detail.html',context={'post':post})
	comments=post.comments.filter(active=True)
	added=False
	if request.method =="POST":
		comment_form=forms.CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.post=post
			new_comment.save()
			added=True
	else:
		comment_form=forms.CommentForm()

	return render(request,'website/post/detail.html',context={'post':post,'comments':comments,'comment_form':comment_form,'added':added})


def share_post(request,id):
	post=Post.published.get(id=id)
	sent=False
	
	if request.method == 'POST':
		print('method is post')
		form=forms.EmailForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			post_url=request.build_absolute_uri(post.get_absolute_url())
			subject=f"{data['name']} ({data['from_email']}) recomment to read {post.title}"
			message=f"read {post.title} at {post_url}\n\n {data['comment']}"
			from_email='mymail@company.com'
			to_email=['yourmail@company.com']
			send_mail(subject,message,from_email,to_email)
			sent=True
	else:
		form=forms.EmailForm()
	context={'sent':sent,'form':form}
	return render(request,'website/post/share_post.html',context)




	