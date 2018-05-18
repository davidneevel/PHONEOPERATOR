import phone_commands as pc
import look_for_hearts as lfh
import look_for_follow_insta as instaFollowers
import phone_coordinates as xy


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
        a += 1

    pc.homeButton()
    pc.zero()
    pc.onOff()


insta_likes()

# pc.type('great pic')
    






# # text mike
# pc.text_mike()

pc.zero()


pc.checkStatus()


def signal_handler(signal, frame):
    zero()
    print 'You pressed Ctrl+C!'
    sys.exit(0)

