from django.db import models
from django.db import models
# Create your models here.
class place(models.Model):
    img = models.ImageField(upload_to='inmakesproject')
    name=models.CharField(max_length=250)

    desc=models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
