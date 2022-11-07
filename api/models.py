from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    short_desc = models.CharField(verbose_name="Краткое описание", max_length=50)
    full_desc = models.TextField(verbose_name="Полное описание")
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

class NewsImage(models.Model):
    article = models.ForeignKey("News", verbose_name="Новость", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="slider_image")
