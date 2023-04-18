from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=256, null=False, blank=False)

    class Meta:
        db_table = 'offers'

    def __str__(self):
        return str(self.name)
