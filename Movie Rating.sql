# Write your MySQL query statement below
SELECT * FROM (
(
SELECT u.name AS results  
FROM Users u  
JOIN (  
SELECT user_id, COUNT(*) as num_ratings  
FROM MovieRating  
GROUP BY user_id  
) mr ON u.user_id = mr.user_id 
ORDER BY mr.num_ratings DESC, u.name ASC   
LIMIT 1  

)
UNION ALL

(
SELECT m.title AS results   
FROM Movies m   
JOIN (   
SELECT movie_id,
       AVG(rating) as avg_rating    
FROM MovieRating mr2     
WHERE YEAR(mr2.created_at) = 2020 AND MONTH(mr2.created_at) = 2     
GROUP BY movie_id      
 )mr ON m.movie_id = mr.movie_id 
ORDER BY avg_rating DESC ,m.title ASC    
LIMIT 1
)
)t;
