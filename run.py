from bot import reddit


def main():
    r = reddit.Reddit()

    sub = r.subreddit # grab subreddit name
    username = r.name # grab bot username
    r.get_config() # grab config from wiki

    print(f"Logged in as {username}")

    r.scan(sub) # scan subreddit


if __name__ == "__main__":
    main()