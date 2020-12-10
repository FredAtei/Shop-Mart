from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField() 

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def filter_by_location(cls,id):
        image_by_location = cls.objects.filter(image_location_id = id)  
        return image_by_location

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=700, default="Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
           

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
