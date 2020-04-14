drop Table views;
drop Table confirm_purchase;
drop TABLE adds;
drop TABLE checkout;
drop TABLE books;
drop TABLE users;
drop TABLE order_track;


drop Table wrote;
drop Table published;
drop TABLE adds;
drop Table views;
drop Table complete_purchase;
drop Table author;
drop Table publisher;
drop TABLE order_track;
drop TABLE checkout;
drop TABLE books;
drop TABLE users;

delete from wrote;
delete from published;
delete from adds;
delete from views;
delete from complete_purchase;
delete from author;
delete from publisher;
delete from order_track;
delete from checkout;
delete from books;
delete from users;



insert into users values ('1', 'Sanjay', 'Das', '99', 'Hong Kong', 'K29AJ5', 'Canada', 'ONT','415-737-1111','sanjaydas@gmail.com','sanjaydas11','admin');
insert into users values ('2', 'Alagu', 'Veerappan', '53', 'Sunnydale', 'K59AK7', 'Canada', 'ONT','932-644-1331','aveerappan@gmail.com','av11','admin2');
insert into users values ('3', 'Daniel', 'Diep', '65', 'Daniel Craig', 'P79NP7', 'Canada', 'ONT','915-333-5531','dandiep@gmail.com','dandiep','admin3');
insert into users values ('4', 'Ian', 'Brown', '77', 'Parkdale', 'H99NP8', 'Canada', 'ONT','915-555-7781','ianbrown@gmail.com','ianb','admin4');
insert into users values ('5', 'David', 'Ong', '13', 'Iceland', 'O9PNZ8', 'Canada', 'ONT','915-699-0082','daveong@gmail.com','daveong','admin5');
insert into users values ('6', 'Chrissy', 'Zhang', '55', 'Parkdale', 'H90NP9', 'Canada', 'ONT','915-134-3300','chrissyzhang@gmail.com','chrissyz','admin6');
insert into users values ('7', 'Iana', 'Smith', '11', 'Hollowbrook', 'I90IP9', 'Canada', 'ONT','312-555-3355','tinasmith@gmail.com','tinasmith','admin7');
insert into users values ('8', 'Rena', 'Tse', '08', 'MagicRoad', 'K90KP9', 'Canada', 'ONT','312-978-3300','renatse@gmail.com','renatse','admin8');

insert into books values ('1','9781234567897', 'Randy Potter And The Prisoner Of Randaband', 'Oct-2000', '15.99','5');
insert into books values ('2','54313578569997', 'Harold Lee And The Half Blood Princess', 'Sept-2001', '15.99','10');
insert into books values ('3','64313578566667', 'Iana Parker And Lively Hallows', 'Dec-2005', '15.99','15');
insert into books values ('4', '33313588566665', 'Daniel Liu And The Gifted Child', 'May-2003', '15.99','3');
insert into books values ('6','14513774456065', 'Game Of Throws: Burning Sun', 'May-2003', '30.99','1');
insert into books values ('7', '64513774456065', 'Game Of Throws: Rising Raven', 'May-2004', '30.99','19');
insert into books values ('8', '74513884453335', 'Game Of Throws: Edge of Water', 'May-2005', '30.99','20');
insert into books values ('9', '445152525253335', 'Cookie Magicians', 'May-2007', '10.99','20');



insert into author values ('1','K.J','Rolling');
insert into author values ('2','Dave','Martin');

insert into publisher values ('1','Teatree@topbooks.com','99', 'Hong Kong', 'K29AJ5', 'Canada', 'ONT','415-737-1111','TeaTree', '555-55-5555555555');
insert into publisher values ('2','riot@therift.com','55', 'Gong Hong', 'K59BJ5', 'Canada', 'ONT','415-737-3333','RiotTree', '343-33-3333333333');

insert into wrote values ('1','1','9781234567897');
insert into wrote values ('1','2','54313578569997');
insert into wrote values ('1', '3','64313578566667');
insert into wrote values ('1', '4', '33313588566665');
insert into wrote values ('2','6','14513774456065'); 
insert into wrote values ('2','7', '64513774456065'); 
insert into wrote values ('2', '8', '74513884453335');
insert into wrote values ('2','9', '445152525253335');



insert into published values ('1','1','9781234567897');
insert into published values ('1','2','54313578569997'); 
insert into published values ('1', '3','64313578566667');
insert into published values ('1', '4', '33313588566665');
insert into published values ('2','6','14513774456065'); 
insert into published values ('2','7', '64513774456065'); 
insert into published values ('2', '8', '74513884453335'); 
insert into published values ('2','9', '445152525253335');




