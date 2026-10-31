-- your query
SELECT min(id), email from person
group by email
order by min(id) asc