from django.urls import path
from . import views
app_name='website'
urlpatterns=[
path('',views.post_list,name='post-list'),
path('<tag_name>/',views.post_list,name='tagged-post-list'),
# path('',views.PostList.as_view(),name='post-list'),
path('detail/<year>/<month>/<day>/<slug>/',views.post_detail,name='detail'),
path('<id>/share/',views.share_post,name='share')

]