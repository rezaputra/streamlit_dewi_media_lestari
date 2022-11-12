show databases;
use clustering_dewi_media_lestari;

select customers.id_customer as id, customers.nama_customer as name, customer_kategori.kategori_customer as customer_categories, region.region,
orders.nama_item as item, order_item_kategori.item_kategori as item_categories, orders.jumlah as quantity, orders.harga as price, order_pembayaran.total_harga as total_purchases, 
order_pembayaran.dp as down_payment, orders.jenis_pembayaran as payment_type, orders.tgl_order as order_date, order_pembayaran.tgl_pelunasan as payment_date
from orders
INNER JOIN order_pembayaran ON order_pembayaran.id_order_pembayaran=orders.order_id_order_pembayaran
INNER JOIN customers ON orders.order_id_customer=customers.id_customer
INNER JOIN customer_kategori ON customer_kategori.id_customer_kategori=customers.id_customer_kategori_fk
INNER JOIN region ON region.id_region=customers.id_region_fk
INNER JOIN order_item ON order_item.id_order_item=orders.id_order_item_fk
INNER JOIN order_item_kategori ON order_item_kategori.id_order_item_kategori=order_item.id_order_item_kategori_fk
order by customers.id_customer;



select customers.id_customer, customers.nama_customer, sum(order_pembayaran.total_harga)
from orders
INNER JOIN order_pembayaran ON order_pembayaran.id_order_pembayaran=orders.order_id_order_pembayaran
INNER JOIN customers ON orders.order_id_customer=customers.id_customer
INNER JOIN customer_kategori ON customer_kategori.id_customer_kategori=customers.id_customer_kategori_fk
INNER JOIN region ON region.id_region=customers.id_region_fk
INNER JOIN order_item ON order_item.id_order_item=orders.id_order_item_fk
INNER JOIN order_item_kategori ON order_item_kategori.id_order_item_kategori=order_item.id_order_item_kategori_fk
group by customers.id_customer
order by customers.id_customer;