
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Resume

# Register your models here.
admin.site.register(User)
UserAdmin.fieldsets += (("Custom fields",{"fields":("phonenumber")}),)
# UserAdmin.fieldsets += (("Custom fields",{"fields":("nickname","profile_pic")}),)
admin.site.register(Resume)