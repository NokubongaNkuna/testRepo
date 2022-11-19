from django.contrib import admin
from article.models import article,Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(article)