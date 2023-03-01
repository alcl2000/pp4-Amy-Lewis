from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['category_id']
    
    def __str__(self):
        return self.title

    def category_desc(self):
        return self.description
    
    @classmethod
    def get_default_pk(cls):
        test, created = cls.objects.get_or_create(
            title='Default Category', 
            defaults=dict(description='This is a test Category'),
        )
        return test.pk


class Tag(models.Model):
    tag_category = models.ForeignKey(Category, 
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
    
    @classmethod
    def get_default_pk(cls):
        test_tag, created = cls.objects.get_or_create(
            title='Default Tag'
        )
        return test_tag.pk


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    slug = models.SlugField(
                            unique=True,
                            max_length=15
                            )
    # various foriegn keys
    post_category = models.ForeignKey(Category, 
                                      on_delete=models.CASCADE,
                                      )
    post_tag = models.ForeignKey(Tag, 
                                 on_delete=models.SET_DEFAULT,
                                 default=Tag.get_default_pk
                                 )
    post_author = models.ForeignKey(User,
                                    on_delete=models.SET_DEFAULT,
                                    default='Anonymous'
                                    )    
    # post content
    post_title = models.CharField(max_length=25)
    post_content = models.TextField()
    post_date = models.DateField(auto_now=True)
    # user interactions
    post_likes = models.ManyToManyField(
                                         User,
                                         related_name='post_likes',
                                         blank=True
                                        )


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    text = models.TextField()
    # foriegn keys
    comment_author = models.ForeignKey(User,
                                       on_delete=models.SET_DEFAULT,
                                       default='Anonymous'
                                       )
    # user interactions
    comment_likes = models.ManyToManyField(User,
                                           related_name='comment_likes',
                                           blank=True
                                           )