drop table if exists posts;
	create table posts (
		content text not null
);

drop table if exists users;
	create table users (
		id integer primary key autoincrement,
		login text not null,
		password text not null
);