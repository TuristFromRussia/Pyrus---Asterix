from datetime import datetime

from events.event_bus import (
    EventBus
)

from events.events import (
    CallStartedEvent
)


def on_call_started(event):

    print(
        f"Звонок от {event.phone}"
    )


event_bus = EventBus()

event_bus.subscribe(
    CallStartedEvent,
    on_call_started
)

event_bus.publish(
    CallStartedEvent(
        phone="+79991112233",
        unique_id="123",
        linked_id="123",
        occurred_at=datetime.now()
    )
)