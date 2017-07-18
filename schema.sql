drop table if exists alert;
    create table alert (
            id integer primary key autoincrement,
            name text not null,
            location text not null
        );
