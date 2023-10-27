-- 코드를 입력하세요
select t1.animal_id, t1.name
from
(SELECT *
from animal_ins
where animal_type = 'Dog'
order by name) as t1
where name like '%el%' or '%El%'
