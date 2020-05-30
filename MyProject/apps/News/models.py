from django.db import models

class Rubric(models.Model):
	name = models.CharField(max_length=30, db_index=True, verbose_name='Категория')

	class Meta:
		verbose_name = 'Категорию'
		verbose_name_plural = 'Категории'
		ordering = ['name']

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=70, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
	rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Категория')

	class Meta:
		verbose_name = 'Статью'
		verbose_name_plural = 'Статьи'
		ordering = ['-published']

	def __str__(self):
		return self.title


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name='Статья')
	author = models.CharField(max_length=30, verbose_name='Автор комментария')
	comment_text = models.CharField(max_length=300, verbose_name='Комментарий')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return self.comment_text