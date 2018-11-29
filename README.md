# redditor 2.0

command line interface for reddit

![demo](https://raw.githack.com/daenylio/redditor/master/demo.svg "demo")

## usage

```bash
Syntax:
redditor [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  feed       Much wow, such interesting.
  subreddit  Show the dogy list.
```

## installation

pre-install

```bash
pip install click
pip install praw
```

in the extracted folder, run:

```bash
pip install --editable .
```

## to do

next version should have:

- [x] unlimited query
- [x] command quit/q/double Enter to quit
- [x] deploy to pip
- [ ] release as .deb
- [x] beautiful .svg
