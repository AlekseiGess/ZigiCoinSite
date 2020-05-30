from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView
from .models import Rubric, Article, Comment
from django.views.generic import View, ListView
from django.urls import reverse
from .forms import CommentForm




def index(request):
	# Главная страничка
	return render(request, 'news/index.html')


def contact(request):
	# Контактная информация
	return render(request, 'news/contact-us.html')


#def articles(request):
	# Выводит список статей.
	#articles = Article.objects.order_by('-published')
	#context = {'articles': articles}
	#return render(request, 'news/articles.html', context)

class ArticlesView(ListView):
	model = Article
	queryset = Article.objects.all()
	template_name = 'news/articles.html'
	context_object_name = 'articles'


class PostDetail(View):
	# Выводит одну статью.
	def get(self, request, article_id):
		article = get_object_or_404(Article, id = article_id)
		latest_comments_list = article.comment_set.order_by('-id')[:10]
		context = {'article': article, 'latest_comments_list': latest_comments_list}
		return render(request, 'news/detail.html', context)


def add_comment(request, article_id):
	# Выводит комментарии.
	try:
		article = Article.objects.get(id = article_id)
	except:
		raise Http404("Article Does Not Exist.")
	article.comment_set.create(author = request.POST['name'], comment_text = request.POST['text'])
	return HttpResponseRedirect(reverse('News:detail', args = (article.id,)))
		