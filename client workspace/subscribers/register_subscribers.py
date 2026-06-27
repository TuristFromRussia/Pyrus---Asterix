from events.events import (
    CallStartedEvent
)

from subscribers.ui_subscriber import (
    on_call_started
)


def register_subscribers(
    event_bus
):

    event_bus.subscribe(
        CallStartedEvent,
        on_call_started
    )

    print(
        "Subscribers registered"
    )