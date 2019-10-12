from .models import Feed_details, Feed


def check_if_post_in_db(title):
    try:
        x = True if Feed.objects.filter(title__iexact=title).exists() else False
    except:
        x = False
        pass
    return x


def update_feed_status(source, message, updated_time):
    try:
        Feed_details.objects.filter(feed_source__iexact=source, status__iexact='Active').update(message=message,
                                                                                                last_updated=updated_time)
    except:
        pass
