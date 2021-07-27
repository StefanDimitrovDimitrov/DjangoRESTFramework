from django.contrib import admin

# Register your models here.
from Articles.web.models import Articles, Source


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
