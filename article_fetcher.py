import os
from collections import Counter

from feedy import Feedy
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

BASE_DIR = os.path.dirname(__file__)
feedy = Feedy(os.path.join(BASE_DIR, 'feedy.dat'))

t = Tokenizer()


def _get_proper_nouns(text):
    return [token.surface for token in t.tokenize(text)
            if token.part_of_speech.startswith('名詞,固有名詞')]


def get_words_from_body(body):
    word_counter = Counter()
    soup = BeautifulSoup(body, "html.parser")
    for child_tag in soup.find('body').findChildren():
        if child_tag.name == 'script':
            continue
        child_text = child_tag.text
        for line in child_text.split('\n'):
            line = line.rstrip().lstrip()
            words = _get_proper_nouns(line)
            if words:
                word_counter.update(words)
    return word_counter


@feedy.add('http://b.hatena.ne.jp/hotentry/it.rss')
def hatena_it(feed_info, entry_info, body):
    print(get_words_from_body(body))


@feedy.add('http://hnrss.org/newest?points=50')
def hacker_news(feed_info, entry_info, body):
    print(entry_info['title'])

if __name__ == '__main__':
    feedy.run()
