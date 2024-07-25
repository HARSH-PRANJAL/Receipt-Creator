Create table Users
(
	id serial primary key,
	name varchar(50),
	email varchar(100),
	mobile integer unique not null,
	gst_number varchar(30)
);

Create table Receipts 
(
	id serial primary key,
	receipt_date timestamp default current_timestamp,
	total_amount decimal(10,2),
	user_id integer references Users(id)
);

create table Items
(
	id serial primary key,
	name varchar(50) not null,
	quantity integer not null,
	price decimal(10,2) not null,
	total_price decimal(10,2) generated always as (quantity*price) stored,
	receipt_id integer references Receipts(id)
);