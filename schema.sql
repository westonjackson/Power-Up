drop table if exists alerts;
    create table alerts (
            id integer primary key autoincrement,
            name text not null,
            time text not null,
            location text not null
        );
