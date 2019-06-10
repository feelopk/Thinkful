--What's the most expensive listing? 
--What else can you tell me about the listing?

SELECT
	name,
	price
FROM sfo_listings
ORDER BY price DESC
LIMIT 1