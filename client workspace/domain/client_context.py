from dataclasses import dataclass

from domain.client import Client
from domain.call import Call
from domain.task import Task
from domain.interaction import Interaction


@dataclass
class ClientContext:

    client: Client

    active_tasks: list[Task]

    recent_calls: list[Call]

    interactions: list[Interaction]