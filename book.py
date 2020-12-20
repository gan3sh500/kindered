
# Get symbols from here : https://unicode-table.com/en/sets/arrow-symbols/
# a tweet in the ebook will be formatted as :
# header (name of author)
# tweet
# line
# tweet ...
# for tweet threads:
# tweet
# arrow down
# tweet
# last tweet
# line


def add_header(document, user_name):
    document += '\n \\'
    document += f'## {user_name}'
    document += '\n \\'
    return document


def add_tweet(document, tweet_text, is_end=True):
    document += f'<center>{tweet_text}</center>'
    document += '\n \\'
    if is_end:
        document += f'{ARROW_DOWN}'
    else:
        document += '<hr>'
    return document

