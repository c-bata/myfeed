from feedy import Feedy
import os

BASE_DIR = os.path.dirname(__file__)
feedy = Feedy(os.path.join(BASE_DIR, 'feedy.dat'))


@feedy.add('http://b.hatena.ne.jp/hotentry/it.rss')
def hatena_it(feed_info, entry_info, body):
    print(entry_info['title'])


@feedy.add('http://hnrss.org/newest?points=50')
def hacker_news(feed_info, entry_info, body):
    print(entry_info['title'])

if __name__ == '__main__':
    feedy.run()
