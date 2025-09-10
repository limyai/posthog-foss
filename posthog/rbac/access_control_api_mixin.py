from typing import TYPE_CHECKING

from posthog.settings import EE_AVAILABLE

if TYPE_CHECKING:
    if EE_AVAILABLE:
        from ee.api.rbac.access_control import AccessControlViewSetMixin
    else:
        from posthog.rbac.access_control_stub import AccessControlViewSetMixin
else:
    if EE_AVAILABLE:
        try:
            from ee.api.rbac.access_control import AccessControlViewSetMixin
        except ImportError:
            from posthog.rbac.access_control_stub import AccessControlViewSetMixin
    else:
        from posthog.rbac.access_control_stub import AccessControlViewSetMixin
