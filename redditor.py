import click
import requests


@click.group()
def cli():
    """
    CLI reddit for breakfast 
    """
    pass


@cli.command()
def feed():
    """
    most upvoted threads from subs pass 24 hours
    """

    file = open('/home/v3spyr/Desktop/CLI-PROJECT/Redditor/subs.txt', 'r') # should be local/relative path
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
        except: # should be unlimited
            warning = 'too much reddit, get back to work!'
            click.echo(click.style(warning, fg='red'))


@cli.command()
@click.argument('sub')
@click.option('--unsub', '-u', is_flag=True, help='unsubscribe')
def subscribe(sub, unsub):
    """
    subscribe/unsubscribe to a subreddit
    """
    file = open('/home/v3spyr/Desktop/CLI-PROJECT/Redditor/subs.txt', 'r')
    subs = file.read().split(',')
    if unsub:
        try:
            subs.remove(sub)
        except:
            click.echo('/r/{} is not in the cool list'.format(sub))
    else:
        subs.append(sub)
        subs = list(set(subs))
    file = open('/home/v3spyr/Desktop/CLI-PROJECT/Redditor/subs.txt', 'w')
    file.write(','.join(subs))
    file.close()


@cli.command()
def subreddits():
    """
    show all /r/
    """
    file = open('/home/v3spyr/Desktop/CLI-PROJECT/Redditor/subs.txt', 'r')
    click.echo(file.read())


if __name__ == "__main__":
    cli()