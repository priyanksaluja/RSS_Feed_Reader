# RSS_Feed_Reader

This project will fetch data from RSS feed and store in database and display it on webpage.

There are 2 tables in tis project:

Feed: Store feed data from url
Feed_details: It contains feed details like url, feed source, last run status and number of records inserted in db
A task is created which will run in every 5 mins and check the feed and will update the database with Delta records.

Feed URL used for in this project: "https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en"

Before Starting this project, make sure you enter below data in Feed_details model:

feed_url: https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en
feed_source: Google News
status: Active
