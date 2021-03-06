from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class ProjectModel(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    Date_Added  = models.DateTimeField(auto_now_add=False, auto_now=True)
    HomeLogo = models.FileField(upload_to="ProjectFront")
    HomeVideo = models.FileField(upload_to="ProjectFront")
    HomeBGP = models.FileField(upload_to="ProjectFront", null=True)
    
    def __unicode__(self):
        return str(self.Date_Added)
    
@receiver(pre_delete, sender=ProjectModel)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.HomeLogo.delete(False)
    instance.HomeVideo.delete(False)
    instance.HomeBGP.delete(False)
    
    
    