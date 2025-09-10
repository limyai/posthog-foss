# isort: skip_file
from posthog.settings import EE_AVAILABLE

if EE_AVAILABLE:
    try:
        from ee.clickhouse.queries.column_optimizer import (
            EnterpriseColumnOptimizer as ColumnOptimizer,
        )
    except ImportError:
        from posthog.queries.column_optimizer.foss_column_optimizer import (  # type: ignore
            FOSSColumnOptimizer as ColumnOptimizer,
        )
else:
    from posthog.queries.column_optimizer.foss_column_optimizer import (  # type: ignore
        FOSSColumnOptimizer as ColumnOptimizer,
    )
