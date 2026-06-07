from dataclasses import dataclass

# прилетело событие 
@dataclass
class NewCallEvent:

    unique_id: str

    linked_id: str

    caller: str

    destination: str


@dataclass
class HangupEvent:

    unique_id: str