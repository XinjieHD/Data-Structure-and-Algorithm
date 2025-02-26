# Write your MySQL query statement below
SELECT department_name AS Department, employee_name AS Employee, salary AS Salary
FROM (
    SELECT e.id, e.name AS employee_name, e.salary, e.departmentId, d.name AS department_name,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) RankedSalaries
WHERE salary_rank <= 3;
