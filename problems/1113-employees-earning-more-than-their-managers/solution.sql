-- your query
SELECT e.name as employee from employees e
join employees m on e.manager_id =m.id
where e.salary > m.salary

