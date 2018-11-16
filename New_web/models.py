from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    name = models.CharField("category_name", max_length = 200)
    count = models.PositiveIntegerField("Total product")

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(Category, related_name = "product", on_delete = models.CASCADE)
    name = models.CharField("product_name", max_length = 120)
    price = models.PositiveIntegerField("price")
    short_description = models.TextField("Short Description")
    full_description = models.TextField("Full Description")
    imege = models.ImageField("Image", default ='default.jpg')

    def get_prev(self):
        return mark_safe(f'<img src = {self.imege.url} width = "40" height = "40" class "image"/>')
    get_prev.short_description = "Image"
