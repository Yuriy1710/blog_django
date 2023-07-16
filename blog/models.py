from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Post ')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='No category')
    body = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.title} {self.author}"
    
    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
    