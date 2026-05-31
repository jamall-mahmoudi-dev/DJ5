from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='Django/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
         return f"{self.name } , {self.email} , {self.created_at}"
    