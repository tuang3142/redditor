import click
import requests

@click.group()
def main():
    """
    Reddit API abuser, mostly from /r/dota2
    """
    pass


@main.command()
@click.argument('subreddit')
@click.option('--limit', '-l', help='number of threads to show')
def hot(subreddit, limit=10):
    """
    Collect hot threads
    """
    url = 'https://www.reddit.com/r/{}/top/.json'.format(subreddit)
    params = {
        'limit':limit
    }
    response = requests.get(url, params=params)
    try:
        items = response.json()['data']['children'] 
        threads = []
        for item in items:
            i = {
                'title': item['data']['title'],
                'score': item['data']['score'],
                'link': 'reddit.com{}'.format(item['data']['permalink'])
            }
            threads.append(i)
        for thread in threads:
            print(thread)
            print('\n')
    except:
        print('too much reddit, back to work')

if __name__ == "__main__":
    main()