from posthog.settings import EE_AVAILABLE

if EE_AVAILABLE:
    try:
        from ee.clickhouse.queries.groups_join_query import GroupsJoinQuery
    except ImportError:
        from posthog.queries.groups_join_query.groups_join_query import GroupsJoinQuery  # type: ignore
else:
    from posthog.queries.groups_join_query.groups_join_query import GroupsJoinQuery  # type: ignore
