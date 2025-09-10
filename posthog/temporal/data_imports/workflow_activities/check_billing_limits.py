import dataclasses
import typing

from django.db import close_old_connections
from temporalio import activity

# EE billing quota limiting removed
from posthog.models.team.team import Team
from posthog.temporal.common.logger import bind_temporal_worker_logger_sync


@dataclasses.dataclass
class CheckBillingLimitsActivityInputs:
    team_id: int
    job_id: str

    @property
    def properties_to_log(self) -> dict[str, typing.Any]:
        return {
            "team_id": self.team_id,
            "job_id": self.job_id,
        }


@activity.defn
def check_billing_limits_activity(inputs: CheckBillingLimitsActivityInputs) -> bool:
    logger = bind_temporal_worker_logger_sync(team_id=inputs.team_id)
    close_old_connections()

    # EE billing limits removed - always allow
    return False
