from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Object(models.Model):
    TYPE_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=223)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='media/logo_of_objects')
    description = models.TextField()
    date = models.DateTimeField()
    views = models.IntegerField(default=0)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
