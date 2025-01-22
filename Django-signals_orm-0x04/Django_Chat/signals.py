from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edits(sender, instance, **kwargs):
    # Check if the message exists (update operation)
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:  # Check if content has changed
                MessageHistory.objects.create(
                    message=old_message,
                    old_content=old_message.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass
