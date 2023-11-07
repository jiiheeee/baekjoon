-- 코드를 입력하세요
SELECT animal_ins.name, animal_ins.datetime
from animal_ins
    left join animal_outs on animal_outs.animal_id = animal_ins.animal_id
where animal_outs.animal_id is null
order by datetime
limit 3
