from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Post, Contact

#Custome signal
from django.dispatch import Signal

# Create a custom signal
custom_signal = Signal()

def custom_signal_handler(sender, instance, **kwargs):
    # Code to perform custom actions
    print("Custom Signal is Triggered!")
    print(instance)
    pass
custom_signal.connect(custom_signal_handler)


@receiver(post_save, sender=User)
def send_registration_notification(sender, instance, created, **kwargs):
    if created:
        # Code to send a notification to the user or admin
        print("Post Save Signal Trigger after Inserting in User Model")
        pass


 
# Pre-save signal handler
@receiver(pre_save, sender=Post)
def pre_save_handler(sender, instance, **kwargs):
    print("Pre-save signal received. About to save:", instance.title)

# Post-save signal handler
@receiver(post_save, sender=Post)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        print("Post-save signal received. New instance saved:", instance.title)
    else:
        print("Post-save signal received. Instance updated:", instance.title)

@receiver(post_delete, sender=Post)
def post_delete_handler(sender, instance, **kwargs):
    print("Post-delete signal received. Instance deleted:", instance.title)