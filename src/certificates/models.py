from django.db import models
from accounts.models import User
from courses.models import Course

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_on = models.DateTimeField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/')