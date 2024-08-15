from django.contrib import admin
from .models import Sub_post,Join_post,Notice,HashTag,likes
# Register your models here.
admin.site.register(Sub_post)
admin.site.register(Join_post)
admin.site.register(Notice)
admin.site.register(HashTag)
admin.site.register(likes)