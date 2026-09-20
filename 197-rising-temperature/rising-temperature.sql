/* Write your PL/SQL query statement below */
SELECT w1.id
FROM Weather w1
WHERE EXISTS (
    SELECT 1
    FROM Weather w2
    WHERE w2.recordDate = w1.recordDate - 1
      AND w1.temperature > w2.temperature
);