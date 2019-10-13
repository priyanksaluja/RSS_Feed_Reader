import feedparser
from datetime import datetime
from .functions import check_if_post_in_db, update_feed_status
from .models import Feed, Feed_details
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(minute="*/5")), name="run_every_5_minutes")
def import_data():
    cnt = 0
    updated_time = datetime.now()
    try:
        feed_source = Feed_details.objects.filter(feed_source__iexact='Google News',
                                                  status__iexact='Active').values('feed_url').last()
        feed_data = feedparser.parse(feed_source['feed_url'].encode('utf-8'))
        if feed_data:
            for post in feed_data.entries:
                post_title = post.title
                post_published_date = datetime.strptime(post.published, "%a, %d %b %Y %H:%M:%S %Z")
                if check_if_post_in_db(post_title):
                    continue
                else:
                    Feed.objects.create(title=post_title, link=post.link,
                                    published_date=post_published_date, source='Google News')
                    cnt+=1

            message = "{} records inserted".format(cnt)
        update_feed_status(source='Google News', message=message,updated_time=updated_time)
    except Exception as e:
        message = "Error - {}".format(e)
        update_feed_status(source='Google News', message=message, updated_time=updated_time)