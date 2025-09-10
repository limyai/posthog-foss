"""Stub implementations for RBAC functionality in FOSS version"""

from django.db import models


class AccessControlViewSetMixin:
    """Stub mixin for access control - no-op in FOSS version"""
    pass


class AccessControlViewMixin:
    """Stub mixin for access control - no-op in FOSS version"""
    pass


def can_user_perform_action(user, action, resource):
    """Always returns True in FOSS version"""
    return True


class AccessControl(models.Model):
    """Stub AccessControl model for FOSS version"""
    class Meta:
        app_label = "posthog"
        managed = False


class Role:
    """Stub Role model for FOSS version"""
    pass


class RoleMembership:
    """Stub RoleMembership model for FOSS version"""
    pass


class OrganizationResourceAccess:
    """Stub OrganizationResourceAccess model for FOSS version"""
    pass