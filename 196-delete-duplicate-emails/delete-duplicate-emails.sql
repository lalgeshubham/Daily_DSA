/* Write your PL/SQL query statement below */
delete from Person where id not in (select min(id) from Person p Group by email)