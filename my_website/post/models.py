from django.db import models


def upload_location(instance, filename):
    return f'{instance.id}, {filename}'



class Post(models.Model):
    title = models.CharField(max_length=30)
    money = models.CharField(max_length=10)
    size = models.CharField(max_length=4)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field='height_field',
                              width_field='width_field',
                              )

    image1 = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field='height_field',
                              width_field='width_field',
                              )

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/posts/detail/{self.id}'
