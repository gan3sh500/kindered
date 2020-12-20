import json

import tweepy


def read_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


def try_tweepy(api_key, api_key_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication: {}".format(e))


if __name__ == '__main__':
    credentials = read_json('credentials.json')
    arguments = ['api_key', 'api_key_secret', 'access_token', 'access_token_secret']
    try_tweepy(*[credentials[x] for x in arguments])
