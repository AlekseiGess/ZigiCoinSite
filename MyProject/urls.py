from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('News.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]