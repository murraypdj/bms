from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=13)
    voip_usage = models.IntegerField()
    sms_usage = models.IntegerField()
    storage_usage = models.IntegerField()
    subscription = models.CharField(max_length=10)
    usage_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_id} - {self.usage_date}"
