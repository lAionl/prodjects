from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=50, uniqie=True, verbose_name="Название")
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(Category)
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " not exist"
        return s

class BlogArticle(models.Model):
    title = models.CharField(unique_for_date="pubdate")
    pubdate = models.DataField()

class BlogArticle(models.Model):
    title = models.CharField(unique_for_month="pubdate")
    pubdate = models.DataField()
    updated = models.DataTimeField(auto_now=True)