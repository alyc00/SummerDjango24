import uuid
from django.db import models
from store.models import Studio, Show


# Create your models here.

class Order(models.Model):
    id = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False) 
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order ({self.id})"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.Order.all())


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, related_name='order items', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    num_of_episodes = models.ForeignKey(Show, on_delete=models.CASCADE)
    type = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.ForeignKey(Show, on_delete=models.CASCADE)

    def get_title(self):
        return f"{self.show.title}"
    
    def get_cost(self):
        return self.price





