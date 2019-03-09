import phone_commands as pc
import look_for_hearts as lfh  #this is the instagram one
import look_for_follow_insta as instaFollowers
import phone_coordinates as xy
import look_for_twit_heart as theart
import look_for_fb_like as lffb
import look_for_reddit_like as lfrl
from time import sleep
from random import randint


# pc.unlock()
# print  "phone unlocked"
# pc.twitter() # note this doesn't include the unlock phone command! 


def twit_likes():
    pc.unlock()
    pc.move(xy.app(3,2))
    pc.tap()
    a = 0
    while a < 20:
        theart.lookForTwitHearts()
        pc.scrollUp()
        pc.getOutTheWay()
        a += 1
    theart.lookForTwitHearts()  # one last lookfor hearts 
    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()

def tweet(a):
    pc.unlock()
    pc.move(xy.app(3,2))
    pc.tap()                # open twitter
    pc.movexy(2850, 3000)  
    pc.lightTap()                # hit tweet button
    sleep(4)  # wait for keyboard to come up
    pc.type(a)
    pc.movexy(2800, 6350)  # hit tweet button
    pc.tap()
    pc.getOutTheWay()
    sleep(5)    
    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()







# STARTINGddsf

def insta_followers():
    pc.unlock() 
    pc.move(xy.app(2,1))
    pc.tap()                # open insta
    sleep(4)                # wait for insta to load
    pc.movexy(2850, 2700)
    pc.tap()                # hit profile
    pc.movexy(2200, 6100)
    pc.tap()                #hit followers
    pc.move(xy.homeButton)
    a = 0
    while a < 15:
        instaFollowers.followBack()
        pc.scrollUp()
        pc.getOutTheWay()
        a += 1
    pc.movexy(950, 6400)
    pc.tap()                   # back to profile
    pc.movexy(1000, 2650)
    pc.tap()     # back to main instagram feed
    pc.homeButton()

def insta_likes():  # Yo! lfh.lookForHearts has the commenting functionality built into it.
    pc.unlock()
    pc.move(xy.app(2,1))  # instagram app
    pc.tap()
    #  look for unliked insta posts
    a = 0
    while a < 20:
        pc.scrollUp()
        pc.getOutTheWay()
        lfh.lookForHearts()
        a += 1

    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()


def reddit_upvote():
    pc.unlock()
    pc.move(xy.app(3,4))
    pc.tap()
    pc.getOutTheWay()
    pc.sleep(2)
    a = 0
    while a < 15:
        pc.scrollUp()
        pc.getOutTheWay()
        lfrl.lookForLikes()
        a += 1
    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()


def fb_likes():
    pc.unlock()
    pc.move(xy.app(2,3))
    pc.tap()
    pc.getOutTheWay()
    pc.sleep(2)
    a = 0
    while a < 15:
        pc.scrollUp()
        pc.getOutTheWay()
        lffb.lookForLikes()
        a += 1
    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()

    
def buienradar():
    pc.unlock()
    pc.move(xy.app(2,5))
    pc.tap()
    pc.getOutTheWay()
    sleep(6)
    pc.homeButton()
    pc.zero()
    sleep(1)
    pc.onOff()


def quit_apps():
    pc.unlock()
    pc.homeButton()  # includes tap command
    pc.tap()
    for x in range(0,4):
        pc.scrollWayUp()
    pc.homeButton()
    sleep(2)
    pc.zero()
    pc.onOff() 
 
def insta_photo():
    pc.unlock()
    pc.insta_photo()
    

                        # THE RANDOMIZER
while 0:
    i = randint(1,100)
    if i < 5:
        print "chose Marktplaats"
        marktplaats()
    elif i < 10:
        print "chose buienradar"
        buienradar()
    elif i < 20:
        print "chose quit apps"
        quit_apps()
    elif i < 25:
        print "going to send a tweet"
        tweet("having a nice time hanging out at #todaysart")
    elif i < 30:
        print "going to send a tweet"
        tweet("if you are at #todaysart come see mee. im at the grey space gallery.")
    elif i < 35:
        print "going to send a tweet"
        tweet("#art #blessed #todaysart")
    elif i < 50:
        print "going to like some instagrams"
        insta_likes()
    elif i < 67:
        print "going to follow some instagrammers"
        insta_followers()
    elif i < 84:
        print "going to look at some tweets"
        twit_likes()
    elif i < 99:
        print "going to like some fbs"
        fb_likes()
    else: 
        print "going to text mike"
        # pc.text_mike()

    sleepTime = randint(15, 300)
    while sleepTime > 0:
        print "going to be social in", sleepTime, "seconds"
        sleepTime -= 1
        sleep(1)
    
# insta_likes()
# insta_followers()
# pc.text_mike()
# twit_likes()
# fb_likes()
# buienradar()
# tweet("shooting a video today")


# pc.insta_selfie()
# quit_apps()

# pc.marktplaats()

# tweet("i will be on display next weekend in the hague at todaysart www.todaysart.nl")

# tweet("having a nice time hanging out at #todaysart")



# pc.text_mike()
# 

# quit_apps()

reddit_upvote()






# # text mike
# pc.text_mike()

# pc.zero()


# pc.checkStatus()


def signal_handler(signal, frame):
    zero()
    print 'You pressed Ctrl+C!'
    sys.exit(0)

