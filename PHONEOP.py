import phone_commands as pc
import look_for_hearts as lfh
import look_for_follow_insta as instaFollowers
import phone_coordinates as xy
import random

# pc.unlock()
# print  "phone unlocked"
# pc.twitter() # note this doesn't include the unlock phone command! 



def insta_selfie():

    pc.unlock()
    pc.insta_selfie() # Opens insta, takes photo. note this doesn't include the unlock phone command! 
    pc.off()

# STARTING

def insta_followers():
    pc.unlock()
    pc.open_insta_followers()
    a = 0
    while a < 15:
        instaFollowers.followBack()
        pc.scrollUp()
        pc.getOutTheWay()
        a += 1
    pc.movexy(1000, 2650)
    pc.tap()     # back to main instagram feed
    pc.homeButton()

def insta_likes():
    pc.unlock()
    pc.move(xy.app(2,1))  # instagram app
    pc.tap()
    #  look for unliked insta posts
    a = 0
    while a < 20:
        pc.scrollUp()
        pc.getOutTheWay()
        lfh.lookForHearts()
        b = random.randint(1,100)
        print "random number = %d" % b
        if b <= 20:
            pc.x(1100)  # move over to the comment button
            pc.type("nice")
            pc.movexy(2800, 4300)  #post comment
            tap()
            pc.movexy(900, 6300)  # back to stream
            tap()
        if b > 20 and b <= 40:
            pc.x(1100)  # move over to the comment button
            pc.type('great pic')
            pc.movexy(2800, 4300)  #post comment
            tap()
            pc.movexy(900, 6300)  #back to stream
            tap()

        a += 1

    pc.homeButton()
    pc.zero()
    pc.onOff()


# insta_likes()

pc.type('great pic')
    






# # text mike
# pc.text_mike()

pc.zero()


pc.checkStatus()


def signal_handler(signal, frame):
    zero()
    print 'You pressed Ctrl+C!'
    sys.exit(0)

