from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    REQUEST_TYPES = [
        ('BILLING', 'Billing Issue'),
        ('TECHNICAL', 'Technical Support'),
        ('CONNECTION', 'New Connection'),
        ('DISCONNECTION', 'Disconnection'),
        ('OTHER', 'Other'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)

    def __str__(self):
        return f"{self.customer.account_number} - {self.request_type} - {self.status}"