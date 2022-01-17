from pol.models.topic import Topic
from pol.permission import Role
from pol.permission.rules import can_view_topic


class UnauthorizedAccessException(Exception):
    pass


def enforce(user_role: Role, topic: Topic):
    rule = can_view_topic

    result, denial_reason = rule(user_role, topic)

    if not result:
        raise

    if ()
