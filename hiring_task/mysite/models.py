from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)

    #def number_of_orders(self):
        #return Order.objects.values('name').count()

    #def total_price_all_order(self):
        #orders_entry = Order.objects.values('name')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()
    manufacturer = models.CharField(max_length=50)
    per_product_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def total_price_per_order(self):
        return self.quantity * self.per_product_price



