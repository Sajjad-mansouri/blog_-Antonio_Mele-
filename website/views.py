from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Post



def post_list(request):

	posts=Post.published.all()
	paginator=Paginator(posts,1)
	page_number=request.GET.get('page')
	page_object=paginator.get_page(page_number)
	return render(request,'website/post/list.html',context={'page_obj':page_object})


def post_detail(request,**kwargs):
	print(kwargs['slug'])

	post=get_object_or_404(Post,slug=kwargs['slug'],
								status='p',
								publish__year=kwargs['year'],
								publish__month=kwargs['month'],
								publish__day=kwargs['day'],
								

												)

	return render(request,'website/post/detail.html',context={'post':post})
