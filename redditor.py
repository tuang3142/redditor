import click
import requests
import os


@click.group()
@click.version_option()
def main():
    """
    command line interface for reddit
    """
    pass


@main.command()
@click.option('--subreddit', '-r', help='feed from a specified subreddit')
def feed(subreddit):
    """
    most upvoted threads from subs pass 24 hours
    """
    if subreddit:
        subs = [subreddit]
    else:
        file = open(filepath('subs.txt'), 'r')
        subs = file.read().split(',')
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
            header = ('/r/' + sub).upper()
            click.echo(click.style(header, fg='cyan', bold=True))
            for thread in threads:
                title = '[{}] {}'.format(thread['score'], thread['title'])
                link = thread['link']
                click.echo(click.style(title, fg='green'))
                click.echo(link)
            click.echo()
        except:
            warning = 'too much reddit, get back to work!'
            click.echo(click.style(warning, fg='red'))


@main.command()
@click.argument('sub')
@click.option('--unsub', '-u', is_flag=True, help='unsubscribe')
def change(sub, unsub):
    """
    subscribe/unsubscribe to a subreddit
    """
    file = open(filepath('subs.txt'), 'r')
    subs = file.read().split(',')
    if unsub:
        try:
            subs.remove(sub)
        except:
            click.echo('/r/{} is not in the cool list'.format(sub))
    else:
        subs.append(sub)
        subs = list(set(subs))
    file = open(filepath('subs.txt'), 'w')
    file.write(','.join(subs))
    file.close()


@main.command()
def all():
    """
    show all /r/
    """
    file = open(filepath('subs.txt'), 'r')
    click.echo(file.read())

# get absolute path to file
def filepath(file):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'subs.txt')
    return path


if __name__ == "__main__":
    main()