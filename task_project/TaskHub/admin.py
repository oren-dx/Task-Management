from django.contrib import admin
from TaskHub.models import*

admin.site.register([UserModel,TaskModel])
