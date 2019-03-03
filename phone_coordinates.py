# xy locations of different points on the screen

homeButton = (1950,2250)

#  SERVO SHIT

servoUp = 65
servoDown = 110
servoDownLight = 101
servoDownSuperLight = 99

#                     APP SCREEN




asCol0 = 1150
asCol1 = 1700
asCol2 = 2250
asCol3 = 2800

asRow0 = 6300
asRow1 = 5760
asRow2 = 5220
asRow3 = 4680
asRow4 = 4140
asRow5 = 3600
asRow6 = 2800


asCols = (asCol0, asCol1, asCol2, asCol3)
asRows = (asRow0, asRow1, asRow2, asRow3, asRow4, asRow5, asRow6)

def app(x,y):
    a = asCols[x]
    b = asRows[y]
    return(a,b)




#                       NUMBER PAD
# x vals
npCol1 = 1250 # 147
npCol2 = 1950 #2580
npCol3 = 2550 #369

# Y vals
npRow1 = 5100 #  top 123
npRow2 = 4632
npRow3 = 4066
npRow4 = 3500 # bottom 0


np0 = (npCol2, npRow4)
np1 = (npCol1, npRow1)
np2 = (npCol2, npRow1)
np3 = (npCol3, npRow1)
np4 = (npCol1, npRow2)
np5 = (npCol2, npRow2)
np6 = (npCol3, npRow2)
np7 = (npCol1, npRow3)
np8 = (npCol2, npRow3)
np9 = (npCol3, npRow3)

#   KEYBOARD

kbRow0 = 3675 # top row
kbRow1 = 3350
kbRow2 = 2975
kbRow3 = 2700 # bottom of phone

space = (2100, kbRow3)
numbers = (900, kbRow3)
delete = (3000, kbRow2)
a = (1000, kbRow1)
b = (2182, kbRow2)
c = (1716, kbRow2)
d = (1475, kbRow1)
e = (1366, kbRow0)
f = (1712, kbRow1)
g = (1950, kbRow1)
h = (2187, kbRow1)
i = (2533, kbRow0)
j = (2425, kbRow1)
k = (2662, kbRow1)
l = (2900, kbRow1)
m = (2650, kbRow2)
n = (2415, kbRow2)
o = (2766, kbRow0)
p = (2950, kbRow0)
q = (900, kbRow0)
r = (1600, kbRow0)
s = (1237, kbRow1)
t = (1833, kbRow0)
u = (2300, kbRow0)
v = (1949, kbRow2)
w = (1100, kbRow0)
x = (1483, kbRow2)
y = (2066, kbRow0)
z = (1250, kbRow2)
one = q
two = w
three = e
four = r
five = t
six = y
seven = u
eight = l
nine = o
zero = p
hashtag = (2975,2700)

period = 0