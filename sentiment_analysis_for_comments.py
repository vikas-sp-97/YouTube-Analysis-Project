from textblob import TextBlob

def get_sentiment_socre(comments_list):
    total_review_polarity = []
    total_review_subjectivity = []
    for comment in comments_list:
        x = TextBlob(comment).sentiment.polarity
        y= TextBlob(comment).sentiment.subjectivity
        total_review_polarity.append(x)
        total_review_subjectivity.append(y)

    # return the average polarity and subjectivity for the list of comments provided
    return sum(total_review_polarity) / len(total_review_polarity), sum(total_review_subjectivity) / len(total_review_subjectivity)

if __name__ == '__main__':
    comments_list = ["Candice has such great humor and sharp wit, I'd love to hear a podcast with her! 🙌",
                     'I honestly dont understand people who hate on Candice. That woman is a BADASS! She has 3 companies, a baby, a family and her people love her! She fell in love with a guy with a kid and loved him as her own. You know how hard that is? Candice, fuck everyone else! You are an inspiration!',
                     "Anyone who was here before this whole youtube vlog thing blew up knows that Candice is the most patient and spontaneous partner. I mean she has to be in order to have been so long with this guy. Candice is just busy fulfilling her life and taking care of a baby to be on every time the camera is out. pretty simple. all the teenage boys who have too much to say don't know what a legit relationship looks like and how much work it is to fight for one and to share your life with another person",
                     "To people who are mean to Candice repeat after me... BEING RESERVED AND CAMERA SHY DOES NOT MAKE HER A DUD OR A MEAN PERSON Watch her girlboss interview she's so funny and sweet.",
                     'Candice you are beautiful and have a great sense of humor Casey is lucky to have you.',
                     'I absolutely would watch that podcast, make it happen! Also, great short film.',
                     'Man that movie was absolutely dope! Keep it up Shantell!',
                     "LOVE the video, thank you, such an incredible story. Also YES to the podcast and I LOVE Candice's presence and energy.",
                     'I absolutely LOOOOOVE the name Candice!!!!!i also love the podcast idea!!',
                     "A lot of hate in the comments for candice. If you have watched Casey for a long time before his vlogs blew up... candice is kind and patient and fun and puts up with a lot from Casey. So what she doesn't smile on camera all the time. Remember she's around Casey 24/7 with his camera. You judging her for seeing her on camera for 2 minutes is ridiculous. Candice keep being you.",
                     'I like her. She seems like she would put Casey in his place lol',
                     "This is a reply to Candice.  You do NOT come across as bitchy or anything negative.  You come across in Casey's videos as passionate about, Casey, Francine, Family, Work, Finn, Billy!, Life, and all the craziness that goes with it.  It constantly amazes me that you do all this despite of and because of Casey's mad genius.  Watch his video's long enough and his love for you and family comes through as the power that drives his life.  They say that behind every great man is a woman.  I say, behind Casey's genius is their is a far more powerful woman with which Casey knows he can't live without.   Bless you both   Always.",
                     "This is a surprisingly motivating video, from beginning to end. Great stuff! She's a great artist, and you guys should DEFINITELY do the podcast ~",
                     "Wow! I love this video, especially the part with Shantell. Thank you Casey for sharing, I think I wouldn't find her channel if you hadn't invited her. She's such an inspiring person! You're my man Casey!",
                     "How dare Candice not be a bubbly, charismatic person! Seriously though, I think it's refreshing to see someone on YouTube who isn't all giggles and sunshine and she certainly shouldn't be pressured by this audience to act differently just to make them more comfortable. Also, thanks for showing that marriages aren't perfect and need work from time to time!!!",
                     'I enjoy listening to your voice. Yes to podcast :)',
                     'If Candice wants to do a podcast because she has something to say or share then yeah do it but if she’s looking to prove something to strangers judging her, no. Anything you do should be done because it brings enrichment to your world (telling Casey things he already knows). My only concern would be you both have your own things that you excel at and I worry that being in each others faces in this shared space could fester other issues.',
                     'Podcast sounds amazing! You always give great advice, sure that would spill over into the cast',
                     'She is so creative! This makes me want to start painting and drawing again (my hands tremble and shake so I had to stop 5 years ago, I am curious to see what I can do with this in my art and maybe find a new way or do a different style to be able to find joy in art again. ♡♡ ) I love that Samsung supported this and is encouraging others to share their "gifts" whether it is art, dancing, cooking, comedy and more.',
                     'Seriously love those stickers and the short film! Both did an amazing job!❤️👍']
    # print(len(comments_list))
    print(get_sentiment_socre(comments_list))