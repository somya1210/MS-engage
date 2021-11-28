from django.contrib import admin
from Users.models import UserProfile,Contact,Task
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(Task)