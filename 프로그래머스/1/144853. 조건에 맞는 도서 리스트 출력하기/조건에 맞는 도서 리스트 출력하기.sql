SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
FROM book
WHERE YEAR(published_date) = '2021' and category = '인문'
order by published_date
