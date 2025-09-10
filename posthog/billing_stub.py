"""Stub implementations for billing and quota limiting in FOSS version"""

from typing import Any, Optional, List, Dict
from enum import Enum


class QuotaResource(Enum):
    """Stub QuotaResource enum"""
    EVENTS = "events"
    RECORDINGS = "recordings"


class QuotaLimitingCaches:
    """Stub for quota limiting caches"""
    pass


def list_limited_team_attributes(team_id: int) -> List[QuotaResource]:
    """Always returns empty list in FOSS version"""
    return []


def update_all_orgs_billing_quotas(dry_run: bool = False) -> tuple[dict, dict]:
    """Stub function - quota limiting is not available in FOSS version"""
    return {"events": [], "recordings": []}, {"events": [], "recordings": []}


class BillingManager:
    """Stub BillingManager for FOSS version"""
    def __init__(self, *args, **kwargs):
        pass
    
    def get_billing(self, *args, **kwargs):
        return None
    
    def update_billing(self, *args, **kwargs):
        return None