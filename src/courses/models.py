from django.db import models
from accounts.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} – {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True)
    resource_file = models.FileField(upload_to='lesson_files/', blank=True, null=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
