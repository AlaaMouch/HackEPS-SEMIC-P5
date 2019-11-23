create table products
  (
    product_id serial not null ,
    sku char(30) not null,
    proddesc lvarchar(8192) not null,
    pricecost decimal(11,2),
    pricesale decimal(11,2),
    unique (product_id)
  );

create table countries
  (
    country_id varchar(2) not null ,
    countryfull varchar(100) not null ,
    telephonecountrycode integer not null ,
    unique (country_id)
  );

create table customers
  (
    customer_id serial not null ,
    company varchar(70) not null ,
    nationalid varchar(20) not null ,
    custname varchar(50),
    streetaddress varchar(100),
    city varchar(100) not null ,
    state varchar(100) not null ,
    zipcode varchar(15) not null ,
    country_id varchar(2) not null ,
    emailaddress varchar(100) not null ,
    telephonenumber varchar(25) not null ,
    unique (customer_id)
  );

create table bills
  (
    bill_id serial not null ,
    billnumber char(15),
    billdate date not null ,
    customer_id integer not null ,
    discount decimal(5,2),
    soonpayment decimal(5,2),
    shippingamount decimal(11,2),
    unique (bill_id)
  );

create table billitems
  (
    billitem_id serial not null ,
    bill_id integer not null,
    product_id integer,
    units decimal(11,2),
    price decimal(11,2),
    discount_1 decimal(5,2),
    discount_2 decimal(5,2),
    unique (billitem_id)
  );