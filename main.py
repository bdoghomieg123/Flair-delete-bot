import praw
import os
import re
import time
from common import clear
from datetime import datetime
from threading import Timer



reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("bdoghomieg123")


def main():
    now = time.time()
    time.sleep(1)
    print(f"Bot started successfully. Bot will act on posts made after {datetime.now()}.")
    time.sleep(5)
    clear()
    if not os.path.isfile("username_log.txt"):
        username_log = []

    else:
        with open("username_log.txt", "r") as f:
           username_log = f.read()
           username_log = username_log.split("\n")
           username_log = list(filter(None, username_log))


    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    else:
        with open("posts_replied_to.txt", "r") as f:
           posts_replied_to = f.read()
           posts_replied_to = posts_replied_to.split("\n")
           posts_replied_to = list(filter(None, posts_replied_to))




    while True:
        for submission in subreddit.new(limit=10):
            if submission.created_utc >= now:
                if submission.link_flair_text == "Request":
                    author = str(submission.author)
                    if author not in username_log:
                        print(f'Bot saw: "{submission.title}"')
                        username_log.append(author)
                        posts_replied_to.append(submission.id)

                    elif submission.id not in posts_replied_to:
                        if author in username_log:
                            posts_replied_to.append(submission.id)
                            comment = submission.reply("You have already submitted a request today. Please try again tomorrow.")
                            comment.mod.distinguish(sticky=True)
                            submission.mod.remove()
                            print(f"{submission.title} was removed. {author} tried to submit more than 1 request in 24 hours")

    with open("username_log.txt", "w") as f:
        for author in username_log:
            f.write(author + "\n")

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
