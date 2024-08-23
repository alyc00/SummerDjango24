import uuid 
from django.urls import reverse 
from django.db import models


# Create your models here.

class Studio(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False) 
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:shows_by_studio', args=[self.id]) 
    

class Show(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False) 
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    description = models.TextField()
    num_of_episodes = models.DecimalField(max_digits=10, decimal_places=1)
    num_of_seasons = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='static/media/show_images/', blank=True)
    type = models.BigIntegerField(max_length=1)    # typical episode length for pricing reasons; 1 = 10 mins or less, 2 = 11-30 mins, 3 = 31-60 mins, 4 = 61-120 mins, 5 = longer than 120 mins
    price = round(((type * num_of_episodes) / 12))
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('store:shows_detail', args=[self.id]) 
    
    def get_price(self):
        return self.price
   



