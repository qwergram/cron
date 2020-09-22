import os
import threading

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Task(models.Model):
    job_name = models.CharField(max_length=255, unique=True)
    run_interval = models.IntegerField()
    executable = models.CharField(max_length=255)

    def __str__(self):
        return self.job_name


@receiver(post_save, sender=Task)
def task_create(sender, instance, created, **kwargs):
    if created:
        threading.Thread(target=os.system, args=(f'python3 worker.py "{instance.job_name}" {instance.run_interval} "{instance.executable}"',)).start()
