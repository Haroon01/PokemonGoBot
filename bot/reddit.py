import praw
import re
import configparser
import json

class Reddit:
    CONFIG_PATH = "./config/config.ini"
    CREDENTIALS_PATH = "./config/creds.ini"

    credentials = configparser.ConfigParser()
    credentials.read(CREDENTIALS_PATH)

    reddit = praw.Reddit(client_id=credentials.get("ACCOUNT", "CLIENT_ID"),
                         client_secret=credentials.get("ACCOUNT", "CLIENT_SECRET"),
                         username=credentials.get("ACCOUNT", "USERNAME"),
                         password=credentials.get("ACCOUNT", "PASSWORD"),
                         user_agent="PokemonGoBot, created by u/ItsTheRedditPolice")


    def __init__(self):
        self.name = self.reddit.user.me()
        self.subreddit = self.credentials.get("SUBREDDIT", "NAME")


    def check_for_code(self, comment, text):
        pattern = re.compile(
            r'\d\d\d\d.?\d\d\d\d.?\d\d\d\d')  # match a group of 4 digits separated by any character. ".?" = there could be a char here, maybe not

        matches = pattern.findall(text[:14])  # search within the first 14 chars of the text

        if len(matches) < 1:  # if no match is found
            return False
        elif len(matches) > 1:  # if more than one code has been found
            return False
        else:  # if a match is found
            # comment.reply(f"Code was found: {matches[0]}")
            return True

    def scan(self, sub):
        for comment in self.reddit.subreddit(sub).stream.comments(skip_existing = True):
            body = comment.body.lower()
            if comment.parent_id == comment.link_id: ## if comment is top level
                print(body)
                body_split = body.split(" ")
                if self.check_for_code(comment, body) and body_split[1] == "[hostingraid]":
                    print("code found")
                else:
                    print("no code found")

    def get_config(self):
        wiki = self.reddit.subreddit(self.subreddit).wiki["PokeBotConfig"]
        f = open(self.CONFIG_PATH, "w")
        f.write(wiki.content_md)
        f.close()
        config = configparser.ConfigParser()
        config.read(self.CONFIG_PATH)
        list = json.loads(config.get("OPTIONS", "list"))

