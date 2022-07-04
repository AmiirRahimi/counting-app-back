from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from .validators import UnicodePhonenumberValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager

# Create your models here.

class CustomUser(AbstractBaseUser):
    # username_validator = UnicodePhonenumberValidator()

    phonenumber = models.IntegerField(
        _('phonenumber'),
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_superuser = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return str(self.phonenumber)


# class CustomUser(AbstractBaseUser):
    
#     phonenumber = models.IntegerField(verbose_name='شماره تماس' , unique=True )
#     Fname = models.CharField(verbose_name='نام' , max_length=150)
#     Lname = models.CharField(verbose_name='نام خانوادگی' , max_length=150)
#     email = models.EmailField(verbose_name='ایمیل' )
#     adress = models.CharField(verbose_name='آدرس' , max_length=500)
#     national_code = models.CharField(max_length=150 , verbose_name='کد ملی')
#     is_newsletteres = models.BooleanField(verbose_name='عضویت در خبر نامه' , default=False)
#     day_stamp = models.IntegerField(verbose_name='روز عضویت')
#     month_stamp = models.IntegerField(verbose_name='ماه عضویت')
#     year_stamp = models.IntegerField(verbose_name='سال عضویت')
    

#     staff = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     superuser = models.BooleanField(default=False)
    

#     USERNAME_FIELD = 'phonenumber'
#     REQUIRED_FIELDS = []    

#     def __str__(self):
#         return str(self.phonenumber)

#     objects = UserManager()

#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_superuser(self):
#         return self.superuser

#     @property
#     def is_ctive(self):
#         return self.active

#     def has_perm(self, perm, obj=None):
#         return self.is_superuser

#     def has_module_perms(self, app_label):
#         return self.is_superuser

#     class Meta:
#         verbose_name = 'کاربر'
#         verbose_name_plural = 'کاربر ها'

#     def fullname(self):
#         return self.Fname+ ' ' + self.Lname  
        
#     def time_last(self):
#         date = jdatetime.date.today()
#         if self.year_stamp == date.year and self.month_stamp == date.month:
#             if self.day_stamp == date.day:
#                 return 'عضویت در امروز'
#             else:
#                 day_last = date.day - self.day_stamp
#                 return f'عضویت در {day_last} روز پیش'
#         elif self.year_stamp == date.year and self.month_stamp < date.month:
#             if self.day_stamp > date.day and 1 < self.month_stamp < 6:
#                 day_last = (31 - self.day_stamp) + date.day
#                 month_last = date.month - self.month_stamp - 1
#                 return f'عضویت در {month_last}ماه و {day_last}روز پیش'
#             elif self.day_stamp > date.day and 6 < self.month_stamp < 11:
#                 day_last = (30 - self.day_stamp) + date.day
#                 month_last = date.month - self.month_stamp - 1
#                 return f'عضویت در {month_last}ماه و {day_last}روز پیش'
#             elif self.day_stamp > date.day and  self.month_stamp == 12:
#                 day_last = (29 - self.day_stamp) + date.day
#                 month_last = date.month - self.month_stamp - 1
#                 return f'عضویت در {month_last}ماه و {day_last}روز پیش'
#             elif self.day_stamp < date.day:
#                 day_last = date.day - self.day_stamp 
#                 month_last = date.month - self.month_stamp
#                 return f'عضویت در {month_last} ماه و {day_last} روز پیش'
#             elif self.day_stamp == date.day:
#                 month_last = month_last = date.month - self.month_stamp
#                 return f'عضویت در {month_last} ماه پیش'
#         elif self.year_stamp == date.year :
#             return 'fix it'
