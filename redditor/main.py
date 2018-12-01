import praw
import click
from pkg_resources import resource_filename


@click.group()
@click.version_option(message='%(version)s')
def cli():
    """
    Use reddit like a doge.
    """
    pass


@cli.command()
@click.option('--subscribe', '-s', help="Subscribe to a subreddit.")
@click.option('--unsubscribe', '-u', help="Unsubscribe to a subreddit.")
def subreddit(subscribe, unsubscribe):
    """
    Show the dogy list.
    """
    filename = resource_filename(__name__, 'subreddits.txt')
    with open(filename, 'r') as f:
        subreddits = f.read().split()

    if subscribe:
        subreddits.append(subscribe)
        subreddits = list(set(subreddits))
    if unsubscribe:
        try:
            subreddits.remove(unsubscribe)
        except:
            click.echo('r/{} is not in the dogy list.'.format(unsubscribe))
    
    if subreddits:
        for subreddit in subreddits:
            click.echo(click.style('r/' + subreddit, fg='green', bold=True))
    else:
        click.echo('Wow, such empty.')

    with open(filename, 'w') as f:
        f.write(' '.join(subreddits))
        f.close()


@cli.command()
@click.option('--subreddit', '-r', help="Read from a subreddit.")
@click.option('--limit', '-l', default=5, help="How much doge you want to read.")
def feed(subreddit, limit):
    """
    Much wow, such interesting. 
    """
    if subreddit:
        subreddits = [subreddit]
    else:
        filename = resource_filename(__name__, 'subreddits.txt')
        with open(filename, 'r') as f:
            subreddits = f.read().split()

    reddit = praw.Reddit(client_id='Jdfpe3WHOsTA4g',
                     client_secret='aRgCzEfD9rNyutM25z9VAUHg6rQ',
                     user_agent='script:redditor:v2.0 (by /u/tuanngg__)')
    
    try:
        if subreddits:
            for subreddit in subreddits:
                click.echo(click.style('r/' + subreddit, fg='green', bold=True))
                submissions = reddit.subreddit(subreddit).top(limit=limit, time_filter='day')
                for submission in submissions:
                    headline = '[{}] {}'.format(submission.score, submission.title)
                    click.echo(click.style(headline, fg='cyan'))
                    link = 'https://www.reddit.com' + submission.permalink
                    click.echo(link)
                click.echo()
        else:
            click.echo('Wow, such empty.')
    except:
        click.echo('Such doge, nice try.')