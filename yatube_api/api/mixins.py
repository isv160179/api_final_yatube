from rest_framework import viewsets

from .permissions import ReadOnly


class PermissionForRetrieveMixin(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()