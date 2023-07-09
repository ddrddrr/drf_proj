from rest_framework.permissions import IsAdminUser
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin:
    permission_classes = [IsAdminUser, IsStaffEditorPermission]
