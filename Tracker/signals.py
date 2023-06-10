from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Attendance, Notification

@receiver(post_save, sender=Attendance)
def create_notification(sender, instance, created, **kwargs):
    if created:
        is_attendee = instance.attend == 1
        title = "Attendance Notification"
        message = "You are marked as an attendee." if is_attendee else "You are marked as absent."
        Notification.objects.create(
            student=instance.student,
            is_attendee=is_attendee,
            title=title,
            message=message
        )
