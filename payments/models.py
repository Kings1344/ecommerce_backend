from django.db import models

from orders.models import Order
class Payment(models.Model):

    STATUS_CHOICES = [

        ('pending','Pending'),

        ('successful','Successful'),

        ('failed','Failed')

    ]

    order = models.OneToOneField(

        Order,

        on_delete=models.CASCADE,

        related_name='payment'

    )

    reference = models.CharField(

        max_length=100,

        unique=True

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='pending'

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    def __str__(self):

        return self.reference