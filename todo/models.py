from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()
    complete = models.BooleanField(default =False)
    exp = models.PositiveIntegerField(default=0)
    complete_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name