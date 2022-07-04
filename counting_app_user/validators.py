from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class UnicodePhonenumberValidator(validators.RegexValidator):
    regex = r'/^09\d{9}$/'
    message = _(
        'Enter a valid phonenumber. This value may contain only numbers, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0