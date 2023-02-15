from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['category_id']
    
    def category_name(self):
        return self.title

    def category_desc(self):
        return self.description