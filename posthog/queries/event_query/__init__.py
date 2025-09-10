from posthog.settings import EE_AVAILABLE

if EE_AVAILABLE:
    try:
        from ee.clickhouse.queries.event_query import EnterpriseEventQuery as EventQuery
    except ImportError:
        from posthog.queries.event_query.event_query import EventQuery  # type: ignore
else:
    from posthog.queries.event_query.event_query import EventQuery  # type: ignore
