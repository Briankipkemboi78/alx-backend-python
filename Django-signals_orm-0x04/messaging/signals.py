from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Check if the message already exists (update case)
        previous_message = Message.objects.get(pk=instance.pk)
        if previous_message.content != instance.content:
            # Log the old content
            MessageHistory.objects.create(
                message=previous_message,
                old_content=previous_message.content,
                timestamp=previous_message.timestamp,
            )
            # Mark the message as edited
            instance.edited = True