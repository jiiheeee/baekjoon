
select t1.user_id, t1.product_id from 

(select count(user_id) as cnt,user_id, product_id
from online_sale
group by user_id, product_id
order by user_id, product_id desc) as t1

where t1.cnt >= 2
