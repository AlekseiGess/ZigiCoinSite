from django.contrib import admin
from .models import Article, Comment, Rubric
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label= 'Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'rubric', 'published')
	list_display_links = ('title', 'rubric')
	search_fields = ('title', 'text')
	form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Rubric)


