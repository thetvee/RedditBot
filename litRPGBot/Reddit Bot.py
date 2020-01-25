import praw
import re
import time
import pprint
import pdb
import os
# I don't think I need os or pdb anymore but keeping here just in case


# Imports stuff

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("litRPG")
# Sets up the reddit bot login and the subreddit called below

def check_comment(comment_id):
    f = open("comments_checked.txt", "r+")
    #Reads the text file, if file doesn't exist makes one
    comments_checked = f.read()
    print(comments_checked)
    if comment_id not in comments_checked:
        posts_checked = comments_checked.split("\n")
        f = open("comments_checked.txt", "a")
        comments_checked.append(comment_id)
        f.close()
        return True
        #If comment ID is not in the file, adds it to the file & returns True
    else:
        f.close()
        return False
        #Otherwise returns False



def check_flair(post_flair):
    if post_flair is None:
        return False
    #If no flair, ignore it
    if post_flair == "Request":
        return True
    #If flair is request, cool
    else:
        return False
    #If flair is anything else, byeeeee

def parse_comments(comment):
    find=re.findall('Reccomendation',comment)
#'Reccomendation' will ultimately be a list referenced from a google doc
    if find !=[]:
        str=(find[0])
        count=int(str[1:3])
        if count > 10:
            count = 10
    else:
        count = 1
        return count
#I dunno what this does yet, I stole it. I think count is the line number in the referenced list?

for submission in subreddit.hot(limit=1):
#    if check_comment(comment.id) and check_flair(comment.flair):
#If flair is 'request' and comment hasn't been done before...
#        parse_comments(comment.body)
    print(submission.link_flair_text)
    print(submission.comments)
#    print(submission.comment)
#    pprint.pprint(vars(submission))





time.sleep(1500)