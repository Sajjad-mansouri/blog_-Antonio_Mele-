from django.urls import path
from . import views

urlpatterns=[
# path('',views.post_list,name='post-list'),
path('',views.PostList.as_view(),name='post-list'),
path('detail/<year>/<month>/<day>/<slug>/',views.post_detail,name='detail')
]