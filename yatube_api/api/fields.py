import base64

from django.core.files.base import ContentFile
from django.utils import timezone
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            name = str(timezone.now()) + '.' + ext
            data = ContentFile(base64.b64decode(imgstr), name=name)
        return super().to_internal_value(data)
