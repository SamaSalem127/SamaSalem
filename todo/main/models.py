from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Section(models.Model):
    title = models.CharField(max_length=50, unique=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    STATUS_CHOICES = [
        ('Not implemented', 'Not implemented'),
        ('Loading', 'Loading'),
        ('Done', 'Done'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not implemented')
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
