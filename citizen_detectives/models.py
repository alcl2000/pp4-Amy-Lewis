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


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, unique=True)
    
    class ColourOptions(models.TextChoices):
        # options for the tag colours 
        RED = 'RED', ('Red')
        ORANGE = 'ORANGE', ('Orange')
        YELLOW = 'YELLOW', ('Yellow')
        GREEN = 'GREEN', ('Green')
        BLUE = 'BLUE', ('Blue')
        PURPLE = 'PURPLE', ('Purple')
        WHITE = 'WHITE', ('White')
        BLACK = 'BLACK', ('Black')
    
    tag_colour = models.CharField(max_length=6,
                                  choices=ColourOptions.choices,
                                  default=ColourOptions.RED,
                                  )
    
    def tag(self):
        return self.title, self.tag_colour