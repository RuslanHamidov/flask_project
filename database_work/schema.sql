create table if not exists posts (
		content text not null
);
create table if not exists users (
		id integer primary key autoincrement,
		logins varchar(255) not null,
		passwords varchar(255) not null
);