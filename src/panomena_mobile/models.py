from django.db import models

from panomena_mobile import fields


class MsisdnField(models.Field):
    """Field for storing MSISDN values."""

    def formfield(self, **kwargs):
        """Returns the appropriate form field for working with
        MSISDN values.
        
        """
        return fields.MsisdnField(**kwargs)
