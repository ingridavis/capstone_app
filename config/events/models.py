from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.CharField(max_length=100)
    date = models.DateField()



# add in photo later
# add in category later