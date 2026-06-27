CREATE TABLE clients (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    phone TEXT UNIQUE NOT NULL,

    name TEXT,

    company TEXT
);

CREATE TABLE calls (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    client_id INTEGER NOT NULL,

    unique_id TEXT NOT NULL,

    linked_id TEXT NOT NULL,

    status TEXT NOT NULL,

    started_at TEXT NOT NULL,

    ended_at TEXT,

    FOREIGN KEY(client_id)
        REFERENCES clients(id)
);

CREATE TABLE recordings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    call_id INTEGER NOT NULL,

    recording_id TEXT NOT NULL,

    storage_path TEXT,

    public_url TEXT,

    FOREIGN KEY(call_id)
        REFERENCES calls(id)
);

CREATE TABLE tasks (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    external_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    status TEXT NOT NULL
);

CREATE TABLE interactions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    client_id INTEGER NOT NULL,

    source TEXT NOT NULL,

    external_id TEXT NOT NULL,

    created_at TEXT NOT NULL,

    FOREIGN KEY(client_id)
        REFERENCES clients(id)
);