-- your query
SELECT c.customer_id, c.name from customers c
left join orders d on c.customer_id = d.customer_id
where d.customer_id is Null
order by c.customer_id asc
