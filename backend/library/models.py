from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Book(models.Model):
    id=models.AutoField(primary_key=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title=  models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField() 
    published_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)
    


