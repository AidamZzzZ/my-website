from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=250, null=True)
    content = models.TextField(null = True)
    publish = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publish']
   

