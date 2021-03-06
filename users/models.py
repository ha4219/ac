from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.shortcuts import reverse


class User(AbstractUser):
    ''' Custom User Model '''
    # need default="contents" or null=True
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        #default = (),
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean")
    )
    
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )
    
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    #date
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default='', blank=True)
    
    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})
    
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            print(secret)
            self.email_secret = secret
            html_message = render_to_string('emails/verify_email.html', {'secret': secret})
            send_mail('Verify dongha', strip_tags(html_message),
                      settings.EMAIL_FROM,
                     [self.email], fail_silently=False, html_message=html_message,)
            self.save()
        return()
        
            