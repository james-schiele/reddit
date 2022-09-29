import praw
import datetime
import pandas as pd

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    user_name="",
    password=""
)

urls = ["https://www.reddit.com/r/pcgaming/comments/vlq4lq/valorant_will_start_listening_to_your_voice_chat/", "https://www.reddit.com/r/dotamasterrace/comments/vocfh2/valorant_listening_in_on_voice_chat_thoughts/"]

created_date = []
id = []
parent_id = []
body = []
permalink = []
subreddit_id = []
submission_id = []
score = []
stickied = []
comment_replies = []

for url in urls:

    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None)

    for comment in submission.comments.list():
        created_date.append(datetime.datetime.fromtimestamp(comment.created_utc))
        id.append(comment.id)
        parent_id.append(comment.parent_id[3:])
        body.append(comment.body)
        permalink.append(comment.permalink)
        subreddit_id.append(comment.subreddit_id)
        submission_id.append(comment.submission)
        score.append(comment.score)
        stickied.append(comment.stickied)

    print(submission.num_comments)

reddit_df = pd.DataFrame({"Created Date":created_date,"Parent ID":parent_id,"ID":id, "Body":body, "Permalink":permalink, "Subreddit ID":subreddit_id,"Submission ID":submission_id, "Score":score, "Stickied":stickied})
reddit_df.to_csv("valorant_monitoring_reddit.csv", index=False)

