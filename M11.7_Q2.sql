--What neighborhoods seem to be the most popular?

SELECT
	id,
	name,
	neighbourhood,
	number_of_reviews,
	CAST(reviews_per_month AS INT),
	availability_365
FROM sfo_listings
WHERE reviews_per_month != 0
ORDER BY reviews_per_month DESC

--Reason for this method : 
--People usually leave reviews with in positive,
--So, if there is a lot of reviews, then it should
--be the most famous place. But the availability and 
--minimum night are different by host, so, it is 
--trustful when we order the list by 'reviews per month'