from django.db import models

class todo(models.Model):
    task = models.CharField('Task', max_length=140)
    done = models.BooleanField('Done', blank=True, null=True, default=False)

    def __str__(self):
        return self.task

class Potd(models.Model):
    image_file = models.ImageField(upload_to='potd')
    


