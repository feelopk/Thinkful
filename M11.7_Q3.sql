--What time of year is the cheapest time to go to San Francisco? 
--What about the busiest?

WITH sfc AS(
	SELECT 
	listing_id,
	calender_date,
	price
	FROM sfo_calendar
), sfl AS(
	SELECT
		id,
		name,
		room_type,
		price
	FROM sfo_listings
)
SELECT
	sfc.listing_id,
	sfl.id,
	sfl.name,
	sfc.calender_date,
	sfl.room_type,
	sfc.price AS price_calendar,
	sfl.price AS listing_price
FROM sfc
JOIN
	sfl
ON
	sfc.listing_id = sfl.id

