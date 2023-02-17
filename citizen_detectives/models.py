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
    
    @classmethod
    def get_default_pk(cls):
        exam, created = cls.objects.get_or_create(
            title='Default Category', 
            defaults=dict(description='This is a test Category'),
        )
        return exam.pk


class Tag(models.Model):
    tag_category = models.ForeignKey('Category', 
                                     to_field='category_id',
                                     default=Category.get_default_pk,
                                     on_delete=models.CASCADE)
    
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
    
    def tag_category_name(self):
        return self.tag_category.title


# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     post_category = models.ForeignKey('Category', on_delete=models.CASCADE)
#     post_tag = models.ForeignKey('Tag', on_delete=models.)