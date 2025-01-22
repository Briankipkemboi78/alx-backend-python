from django.db.models.signals import post_save, pre_save
from django.db.models.signals import post_delete
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

@receiver(post_delete, sender=User)
def clean_up_user_data(sender, instance, **kwargs):
    # Delete all messages where the user is the sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete all notifications for the user
    Notification.objects.filter(user=instance).delete()

    # Delete all message histories for the user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
