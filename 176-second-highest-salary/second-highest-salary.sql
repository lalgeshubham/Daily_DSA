# Write your MySQL query statement below

select  (
Select distinct(salary) as SECONDHIGHESTSALARY from Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) as SECONDHIGHESTSALARY