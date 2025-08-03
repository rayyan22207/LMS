from django.db import models
from accounts.models import User

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paddle_id = models.CharField(max_length=100, unique=True)
    plan_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    last_payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} – {self.plan_name}"
