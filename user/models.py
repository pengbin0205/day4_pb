from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=60, unique=True,null=False)
    password = models.CharField(max_length=60,null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


