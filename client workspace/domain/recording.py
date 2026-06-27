from dataclasses import dataclass


@dataclass
class Recording:

    id: int | None

    call_id: int

    recording_id: str

    storage_path: str

    public_url: str | None = None