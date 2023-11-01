-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d') as hire_ymd
from doctor
where MCDP_CD = 'GS' or  mcdp_cd = 'CS'

order by hire_ymd desc;