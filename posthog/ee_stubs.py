"""Comprehensive stub implementations for all EE features in FOSS version"""

from typing import Any, Optional, List, Dict, Tuple
from django.db import models
from rest_framework import serializers


# Hook stubs
class Hook(models.Model):
    """Stub Hook model"""
    class Meta:
        app_label = "posthog"
        managed = False


def create_zapier_hog_function(*args, **kwargs):
    """Stub function for zapier hog function creation"""
    return None


# Assistant/AI stubs
class CoreMemory(models.Model):
    """Stub CoreMemory model for AI assistant"""
    class Meta:
        app_label = "posthog"
        managed = False


class Conversation(models.Model):
    """Stub Conversation model"""
    class Meta:
        app_label = "posthog"
        managed = False


# Materialized columns stubs
def materialize(*args, **kwargs):
    """Stub function for materializing columns"""
    pass


def get_enabled_materialized_columns(*args, **kwargs):
    """Stub function returning empty list"""
    return []


# Experiments stubs
class ExperimentResult:
    """Stub for experiment results"""
    pass


class FunnelExperimentResult:
    """Stub for funnel experiment results"""
    pass


class TrendExperimentResult:
    """Stub for trend experiment results"""
    pass


# Test mixin stubs  
class LicensedTestMixin:
    """Stub mixin for licensed tests"""
    pass


# RBAC stubs (additional to what's in access_control_stub.py)
class FeatureFlagRoleAccess(models.Model):
    """Stub for feature flag role access"""
    class Meta:
        app_label = "posthog"
        managed = False


class ExplicitTeamMembership(models.Model):
    """Stub for explicit team membership"""
    class Meta:
        app_label = "posthog"
        managed = False


# License stub
class License(models.Model):
    """Stub License model"""
    class Meta:
        app_label = "posthog"
        managed = False
    
    @classmethod
    def objects(cls):
        class Manager:
            def first_valid(self):
                return None
        return Manager()