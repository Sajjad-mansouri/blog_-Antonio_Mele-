from django.shortcuts import render
from .models import Post



def post_list(request):

	posts=Post.published.all()
	return render(request,'website/post/list.html',context={'post':posts})


def post_detail(request):

	post=get_object_or_404(Post,slug=slug,
								status='p',
								publish__yeaer=year,
								publish__month=month,
								publisih__day=day,

												)

	return render(request,'website/post/detail.html',context={'post':post})
