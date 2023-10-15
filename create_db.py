'''
CREATE TABLE users (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      INTEGER NOT NULL
                         UNIQUE,
    name         TEXT    NOT NULL,
    vip          INTEGER DEFAULT (1),
    start_time   TEXT    NOT NULL,
    end_time     TEXT    NOT NULL,
    active       INTEGER DEFAULT (1),
    refer_id     INTEGER DEFAULT None,
    bill_id      INTEGER DEFAULT (0),
    professional TEXT    DEFAULT [1]
);
'''