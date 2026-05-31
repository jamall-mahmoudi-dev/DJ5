from django.db import models

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']  
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'
    
    def __str__(self):
        return f"{self.name } , {self.email} , {self.created_at}"