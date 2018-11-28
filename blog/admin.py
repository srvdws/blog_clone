from django.contrib import admin
from . import models


admin.site.register(models.PostModel)
admin.site.register(models.CommentModel)
