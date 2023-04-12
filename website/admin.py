from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=['title','slug','author','publish','status']
	list_filter=['author','created','publish','status']
	search_fields=['title','description']
	prepopulated_fields={'slug':('title',)}
	raw_id_fields=['author']
	date_hierarchy='publish'
	ordering=['status','-publish']


admin.site.register(Post,PostAdmin)
