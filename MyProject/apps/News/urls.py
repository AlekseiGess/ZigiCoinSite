from django.urls import path
from . import views
from .views import *

app_name = 'News'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('articles/', ArticlesView.as_view(), name = 'articles'),
	path('article/<int:article_id>/', PostDetail.as_view(), name = 'detail'),
	path('contact-us/', views.contact, name = 'contact'),
	path('article/<int:article_id>/add_comment/', views.add_comment, name = 'add_comment'),

]