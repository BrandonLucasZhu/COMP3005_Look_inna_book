create table users
	(id		varchar(15),
	 firstname		varchar(20),
     lastname		varchar(20),
	 street_num		numeric(10,0),
     street_name	varchar(20),
     postalcode     varchar(15),
     country        varchar(20),
     province       varchar(20),
     phone_number       varchar(20),
     email          varchar(25),
	 username       varchar(20),
	 password       varchar(20),
	 primary key (id)
	);

create table books
	(book_id			varchar(15), 
	 isbn		varchar(20),
	 title		varchar(100),
     publication_date varchar(20),
     price      numeric(10,2),
	 book_stock integer,
	 primary key (book_id, isbn)
	);

create table author
(
	a_id        varchar(15),
	firstname		varchar(20), 
	lastname		varchar(20),
	primary key (a_id)
);

create table publisher
(
	p_id        varchar(15),
	email          varchar(25),
	street_num		numeric(10,0),
    street_name	varchar(20),
    postalcode     varchar(15),
    country        varchar(20),
    province       varchar(20),
    phone_number       varchar(20),
	publisher_name		varchar(20),
	bank_acc varchar(20),
	primary key (p_id)
);

create table checkout
	(c_out_id		varchar(15), 
	 creditcard     varchar(20),
	 date		varchar(30), 
	 shipping_price      numeric(10,2),
     total          numeric(10,2),
	 primary key (c_out_id)
	);

create table order_track
	(order_id		varchar(15), 
	 orderdate     varchar(20),
	 depart_date		varchar(30), 
	 est_arrival      varchar(30), 
     current_location          varchar(30), 
	 primary key (order_id)
	);


create table complete_purchase
	(c_out_id		varchar(15), 
	 order_id     varchar(15),
	 total          numeric(10,2), 
	 primary key (c_out_id, order_id),
	 foreign key (order_id) references order_track,
	 foreign key (c_out_id) references checkout
	);

create table wrote
(
	a_id varchar(15),
	book_id varchar(15),
	isbn varchar(20),
	foreign key (a_id) references author,
	foreign key(book_id, isbn) references books

);

create table published
(
	p_id		varchar(15),
	book_id  varchar(15),
	isbn varchar(20),
	primary key(p_id, book_id),
	foreign key (p_id) references publisher,
	foreign key (book_id, isbn) references books
);

create table views
	(	id		varchar(15),
		c_out_id  varchar(15),
		primary key(id, c_out_id),
		foreign key (id) references users,
		foreign key (c_out_id) references checkout
	);


create table adds
	(c_out_id  varchar(15),
	book_id			varchar(15), 
	isbn		varchar(20),
	foreign key (c_out_id) references checkout,
	 foreign key (book_id, isbn) references books
	);


