from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



CATEGORY_CHOICES = (
    ('food', 'Food'),
    ('jewelry', 'Jewelry'),
    ('produce', 'Produce'),
    ('clothing', 'Clothing'),
    ('yardsale', 'Yardsale'),
    ('other', 'Other'),
)

class Event(models.Model):
    
    title=models.CharField(max_length=100)
    
    description=models.TextField()
    location=models.CharField(max_length=100)
    date=models.DateField()
    category=models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="other")
    photo=models.ImageField(default='no-image-found.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk':self.pk})
    
    def snippet(self):
        return self.description[:50] + '...'
        # taking the first 50 characters to display
    
    



#after making changes to models --- do this:
# python3 manage.py makemigrations
# python3 manage.py migrate