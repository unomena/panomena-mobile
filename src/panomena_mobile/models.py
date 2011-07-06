from django.db import models

from panomena_mobile import fields


class MsisdnField(models.CharField):
    """Field for storing MSISDN values."""

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 32
        super(MsisdnField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        """Returns the appropriate form field for working with
        MSISDN values.
        
        """
        return fields.MsisdnField(**kwargs)
