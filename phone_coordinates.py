# xy locations of different points on the screen

homeButton = (2100,2300)

#  SERVO SHIT

servoUp = 65
servoDown = 110
servoDownLight = 105
servoDownSuperLight = 99

#                     APP SCREEN




asCol0 = 1300
asCol1 = 1850
asCol2 = 2400
asCol3 = 2950

asRow0 = 6300
asRow1 = 5800
asRow2 = 5200
asRow3 = 4700
asRow4 = 4200
asRow5 = 3700
asRow6 = 3000

asCols = (asCol0, asCol1, asCol2, asCol3)
asRows = (asRow0, asRow1, asRow2, asRow3, asRow4, asRow5, asRow6)

def app(x,y):
    a = asCols[x]
    b = asRows[y]
    return(a,b)




#                       NUMBER PAD
# x vals
npCol1 = 1500 # 147
npCol2 = 2100 #2580
npCol3 = 2700 #369

# Y vals
npRow1 = 5300 #  top 123
npRow2 = 4800
npRow3 = 4200
npRow4 = 3700 # bottom 0


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

kbRow0 = 3850
kbRow1 = 3500
kbRow2 = 3100
kbRow3 = 2700

space = (2100, kbRow3)
a = (1200, kbRow1)
b = (2400, kbRow2)
c = (1850, kbRow2)
d = (1700, kbRow1)
e = (1600, kbRow0)
f = (1900, kbRow1)
g = (2100, kbRow1)
h = (2350, kbRow1)
i = (2700, kbRow0)
j = (2600, kbRow1)
k = (2800, kbRow1)
l = (3000, kbRow1)
m = (2800, kbRow2)
n = (2600, kbRow2)
o = (3000, kbRow0)
p = (3100, kbRow0)
q = (1100, kbRow0)
r = (1800, kbRow0)
s = (1400, kbRow1)
t = (2000, kbRow0)
u = (2500, kbRow0)
v = (2100, kbRow2)
w = (1300, kbRow0)
x = (1700, kbRow2)
y = (2200, kbRow0)
z = (1400, kbRow2)
period = 0