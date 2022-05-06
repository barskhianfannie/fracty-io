from django.db import models

# Create your models here.

from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from real_estate.models import House
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def user_directory_path(instance, filename):
    return 'users/avatars/{0}/{1}'.format(instance.user.id, filename)


# Custom validator to validate the maximum size of images


class Profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    # tokens = models.ManyToOneRel()
    houses = models.ManyToManyField(House)
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    active= models.BooleanField(choices=BOOL_CHOICES,default=False, null=True,blank=True)




    def clean(self):
        if not self.avatar:
            raise ValidationError("x")
        else:
            w, h = get_image_dimensions(self.avatar)
            if w >1000:
                raise ValidationError("x")
            if h> 1000:
                raise ValidationError("x")

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
