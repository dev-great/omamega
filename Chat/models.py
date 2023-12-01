from django.db import models

# Create your models here.


class Communication(models.Model):
    message = models.TextField()
    date_sent = models.DateTimeField()
    is_read = models.BooleanField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-date_sent']
