from django.shortcuts import render,get_object_or_404
from .models import Post



def post_list(request):

	posts=Post.published.all()
	return render(request,'website/post/list.html',context={'posts':posts})


def post_detail(request,**kwargs):
	print(kwargs['slug'])

	post=get_object_or_404(Post,slug=kwargs['slug'],
								status='p',
								publish__year=kwargs['year'],
								publish__month=kwargs['month'],
								publish__day=kwargs['day'],
								

												)

	return render(request,'website/post/detail.html',context={'post':post})
