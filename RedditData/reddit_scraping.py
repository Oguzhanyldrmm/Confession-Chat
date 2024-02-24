import praw

# Reddit API
reddit = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='user_agent')

subreddit = reddit.subreddit('confession') #I choose confession subreddit for scraping data.


#List for storing top posts and comments which get most votes.
posts_and_top_comments = []

for submission in subreddit.top(time_filter='all', limit=500): #Limited posts only 500.
    submission.comment_sort = 'top'  # Sort comments by most voted 
    submission.comments.replace_more(limit=0)  # Limit for more comment
    top_comment = next(iter(submission.comments), None)
    if top_comment is not None:
        posts_and_top_comments.append((submission.title, top_comment.body))

# Save to file
with open('dataset.txt', 'w', encoding='utf-8') as f:
    for post, comment in posts_and_top_comments:
        f.write(f"Post: {post}\nTop Comment: {comment}\n\n")

