from django.db import models


class Product(models.Model):
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def short_title(self):
        return str(self.title).split()[0]

    def discount_price(self):
        return float(self.price) * 0.7
