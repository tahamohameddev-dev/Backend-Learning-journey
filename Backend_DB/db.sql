
--find the total sales of each salesman

SELECT SUM(total_sales), client_id
FROM work_with
GROUP BY client_id;
