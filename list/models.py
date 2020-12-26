from django.db import models


# Create your models here.
class Item(models.Model):
    ITEM_STATES = (
        ("BOUGHT", "Bought"),
        ("NOT AVAILABLE", "Unavailable"),
        ("PENDING", "Pending"),
    )

    item_name = models.CharField(help_text="Item name", max_length=30, unique_for_date="date_created", null=False, blank=False)
    quantity = models.CharField(help_text="Quantity", max_length=15)
    item_status = models.CharField(max_length=13, choices=ITEM_STATES)
    date_created = models.DateField(auto_now=False, null=False, blank=False)

    def __str__(self):
        return self.item_name

