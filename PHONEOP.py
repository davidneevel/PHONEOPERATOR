import phone_commands as pc
import look_for_hearts as lfh
import look_for_follow_insta as instaFollowers

# pc.unlock()
# print  "phone unlocked"
# pc.twitter() # note this doesn't include the unlock phone command! 

# pc.insta() # Opens insta, takes photo. note this doesn't include the unlock phone command! 

# STARTING
pc.zero()

# # look for insta followers to follow
# a = 0
# while a < 10:
#     instaFollowers.followBack()
#     pc.scrollUp()
#     pc.getOutTheWay()
#     a += 1


#  look for unliked insta posts
a = 0
while a < 20:
    pc.scrollUp()
    pc.getOutTheWay()
    lfh.lookForHearts()
    a += 1


# # text mike
# pc.text_mike()

pc.zero()


pc.checkStatus()


def signal_handler(signal, frame):
    zero()
    print 'You pressed Ctrl+C!'
    sys.exit(0)

