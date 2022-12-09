from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField
 
 
class Post(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.IntegerField(null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='Pages', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        unique_together = (
            "name",
            "code",
        )
        ordering = ["-created_at"]
 
    def __str__(self):
        return f"Post: {self.name} | code: {self.code}"
 
 
class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 


# Create your models here.
