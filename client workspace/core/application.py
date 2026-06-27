from core.container import (
    Container
)

from subscribers.register_subscribers import (
    register_subscribers
)


class Application:

    def __init__(self):

        self.container = Container()

    def start(self):

        register_subscribers(
            self.container.event_bus
        )

        print(
            "Application started"
        )
    
    def test_call(self):
        self.container.asterisk_simulator.simulate_call(
            "+79991112233"
        )

        