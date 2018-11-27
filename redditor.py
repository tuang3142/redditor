import click
import requests

class colors:
    HEADER = '\033[93m' + '\033[1m'
    TITLE = '\033[92m'
    END = '\033[0m'
    WARNING = '\033[93m'

@click.group()
def main():
    """
    CLI reddit for breakfast 
    """
    pass

@main.command()
def feed(subs):
    for sub in subs:
        url = 'https://www.reddit.com/r/{}/hot/.json'.format(sub)
        params = { 'limit':5 }
        response = requests.get(url, params=params)
        try:
            items = response.json()['data']['children'] 
            threads = []
            for item in items:
                threads.append({
                    'title': item['data']['title'],
                    'score': item['data']['score'],
                    'link': 'http://reddit.com' + item['data']['permalink']
                })
            print(colors.HEADER + '/r/{}'.format(sub) + colors.END)
            for thread in threads:
                title = colors.TITLE + '[{}] {}'.format(thread['score'], thread['title']) + colors.END
                link = thread['link']
                print(title, '\n', link)
            print()
        except:
            print(colors.WARNING + 'too much reddit, back to work!' + colors.END)

@main.command()
