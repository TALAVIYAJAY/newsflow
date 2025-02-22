from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    source = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    summary = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'news_articles'
        ordering = ['-published_at']

    def __str__(self):
        return self.title