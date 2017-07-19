drop table if exists alerts;
    create table alerts (
            id integer primary key autoincrement,
            name text not null,
            time text not null,
            location text null,
            lat integer null,
            long integer null,
            description text null
            anonymous integer not null
        );
