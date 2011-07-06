import re

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


MSISDN_RE = re.compile(r'^[^\d]*(0|\d{2})[ ]*([\d ]+)[^\d]*$')


class MsisdnField(forms.Field):
    """Field for capturing and processing MSISDN values."""
    default_error_messages = { 
        'invalid': _(u'Enter a valid mobile number.'),
        'invalid_country_code': _(u'Enter a number with the %s country code.'),
        'too_short': _(u'Enter a mobile number with more digits.'),
        'too_long': _(u'Enter a mobile number with less digits.'),
    }

    def __init__(self, default_country_code=None, restrict_country_code=None,
                 max_length=11, min_length=11, *args, **kwargs):
        super(MsisdnField, self).__init__(*args, **kwargs)
        self.restrict_country_code = restrict_country_code
        self.default_country_code = default_country_code
        self.max_length = max_length
        self.min_length = min_length

    def to_python(self, value):
        error_messages = self.error_messages
        # check for empty value
        if value in validators.EMPTY_VALUES:
            return None
        # validate the value
        match = MSISDN_RE.match(value)
        # check for an invalid country code
        if match is None:
            raise ValidationError(error_messages['invalid'])
        # ready the groups
        groups = match.groups()
        # determine the country code
        restrict = self.restrict_country_code
        if self.default_country_code and groups[0] == '0':
            country_code = self.default_country_code
        elif restrict and groups[0] == '0': 
            country_code = restrict
        else:
            country_code = groups[0]
            # check for valid country code
            if restrict and country_code != restrict:
                raise ValidationError(
                    error_messages['invalid_country_code'] % restrict
                )
        # remove spaces
        number = groups[1].replace(' ', '')
        # check the length of the msisdn
        msisdn = country_code + number
        if len(msisdn) > self.max_length:
            raise ValidationError(error_messages['too_long'])
        if len(msisdn) < self.min_length:
            raise ValidationError(error_messages['too_short'])
        # return the msisdn
        return country_code + number
    
    def clean(self, value):
        return super(MsisdnField, self).clean(value)


