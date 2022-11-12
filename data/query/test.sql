select * from customers;

select * from region;

select * from customer_kategori;

select harga, jumlah, order_id_customer, total_harga_ex from orders order by order_id_customer;
select * from orders where jenis_pembayaran !=0;
select * from orders;

select * from order_item;
select * from order_item where status_item !=0;


select * from order_pembayaran;
select * from order_pembayaran where total_harga != total_bayar;

select * from order_item_kategori;


select orders.order_id_customer, customers.id_customer, customers.nama_customer, customer_kategori.kategori_customer, region.region, orders.nama_item
from orders
INNER JOIN customers ON orders.order_id_customer=customers.id_customer
INNER JOIN customer_kategori ON customer_kategori.id_customer_kategori=customers.id_customer_kategori_fk
INNER JOIN region ON region.id_region=customers.id_region_fk
order by customers.id_customer;


show tables;

