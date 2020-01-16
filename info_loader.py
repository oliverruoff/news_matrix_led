from datetime import datetime, timezone
import os
import feedparser
import pyowm


def _replace_umlaut(text):
    text = text.replace('ä', 'ae')
    text = text.replace('ö', 'oe')
    text = text.replace('ü', 'ue')
    text = text.replace('ß', 'ss')
    return text


def _utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def get_time():
    """Returns the current (system) time like this: '08.Oct. 14:50'

    Returns:
        str -- Current system time like e.g.: '08.Oct. 14:50'
    """
    return datetime.now().strftime('%d.%b. %H:%M')


def get_tagesschau_rss_feed(last_n_titles=5,
                            news_separator=' | ',
                            rss_url='http://www.tagesschau.de/xml/rss2'):
    """Loads the rss2 feed from tagesschau and returns the last <last_n_titles>
    titles
    and their published dates.

    Keyword Arguments:
        last_n_titles {int} -- The last n titles to be returned (default: {5})
        news_separator {str} -- The seperator used in between the
        titles (default: {' | '})
        rss_url {str} -- The url pointing to the rss2 feed to be parsed
        (default: {'http://www.tagesschau.de/xml/rss2'})

    Returns:
        str -- String including the n requested titles and their
        published dates.
    """
    led_str = ''
    try:
        feed = feedparser.parse(rss_url)
        for post in feed.entries[:last_n_titles]:
            led_str += (_utc_to_local(datetime(
                *post.published_parsed[:6])).strftime('%H:%M') +
                ' ' + _replace_umlaut(post.title) +
                news_separator)
    except:
        led_str = 'Could not load rss feed.'
    return led_str
