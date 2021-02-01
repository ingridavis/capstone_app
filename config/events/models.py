from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    CHOICES =(
        ('Food'),
        ('Produce'),
        ('Clothing'),
        ('Jewelry'),
        ('Other')
    )
    title=models.CharField(max_length=100)
    slug=models.SlugField(null=True, blank=True)
    description=models.TextField()
    location=models.CharField(max_length=100)
    date=models.DateField()
    category=models.ChoiceField(default="DEFAULT VALUE")
    thumb=models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)



    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:50] + '...'
        # taking the first 50 characters to display
        
# add in photo later
# add in category later


#after making changes to models --- do this:
# python3 manage.py makemigrations
# python3 manage.py migrate