from django.db import models
from django.contrib.auth.models import User

class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="savings")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    target = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.target}: {self.amount} on {self.date}"
