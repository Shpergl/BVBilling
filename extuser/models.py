# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, password=None):
        """
        Creates and saves a User with the given fields.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, password):
        """
        Creates and saves a superuser with the given fields.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    PLATOON = (
        ('1rr','1 Рота'),
        ('2rr','2 Рота'),
        ('3rr','3 Рота'),
        ('4rr','4 Рота'),
        ('brr', 'Рота відсутня'),
    )
    SQUADRON = (
        ('1rvz', '1 Взвод'),
        ('2rvz', '2 Взвод'),
        ('3rvz', '3 Взвод'),
        ('4rvz', '4 Взвод'),
        ('5rvz', '5 Взвод'),
        ('brvz', ' Взвод відсутній'),
    )
    SQUAD = (
        ('1rv', '1 Відділення'),
        ('2rv', '2 Відділення'),
        ('3rv', '3 Відділення'),
        ('4rv', '4 Відділення'),
        ('5rv', '5 Відділення'),
        ('brv', 'Відділення відсутне'),
    )
    SPECIALIZATION = (
        ('financier', 'Фінанси'),
        ('logist', 'Тилове забеспечення'),
        ('miner', 'Сапер'),
        ('fizo', 'Фізо'),
    )

    call_name = models.CharField(verbose_name='Позивний', null=True, max_length=100)
    last_name = models.CharField(verbose_name='Прізвище', max_length=100)
    first_name = models.CharField(verbose_name='Ім\'я',max_length=100)
    middle_name = models.CharField(verbose_name='По батькові',null=True, max_length=100)
    bv_id = models.IntegerField(verbose_name='Номер жетона',null=True, unique=True)
    date_of_birth = models.DateField(verbose_name='Дата народження',)
    cell = models.CharField(verbose_name='Контактний телефон',null=True, max_length=100)
    add_email = models.EmailField(verbose_name='Додатковий email',null=True, max_length=50)
    platoon = models.CharField(verbose_name='Рота',null=True, choices=PLATOON, max_length=20)
    squadron = models.CharField(verbose_name='Взвод',null=True, choices=SQUADRON, max_length=20)
    squad = models.CharField(verbose_name='Відділення',null=True, choices=SQUAD, max_length=20)
    specialization = models.CharField(verbose_name='Спеціалізація',null=True, choices=SPECIALIZATION, max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'last_name', 'first_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
@receiver(post_save, sender=MyUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()