from django.db import models

class Order(models.Model):
    SIZE = (
        ('M', '30 cm'),
        ('L', '50 cm'),
    )
    pizza_id = models.PositiveSmallIntegerField ()
    pizza_size = models.CharField(max_length=1, choices=SIZE)
    customer_name = models.CharField(max_length=140)
    customer_address = models.TextField()

    def __str__(self):
        return self.customer_name