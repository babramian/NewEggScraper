# NewEggScraper
Web Scraper for New Egg's search results for "graphics card".

This Scraper scans graphics card listings from this url:
https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards
and looks to pull certain bits of information from each listing.

In specific, the items name, it's brand name, current price, average and amount of ratings, original price (if on sale), number of offers, and shipping price are grabbed and displayed in the prompt. They're also written into a .csv file.

This was fully done in Python using the Beautiful Soup library.
