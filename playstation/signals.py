from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Use this token to reset your password:{}".format(reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for your {title} account".format(title="FINESSE ENT"),
        # message:
        email_plaintext_message,
        # from:
        "abdihakim.0017@gmail.com",
        # to:
        [reset_password_token.user.email]
    )

