#Function File

def polygon( t ,side, distance):
    angle = 360 / side
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    

	
def pi3(i3):
    side = 8
    angle = 135
    distance = 100

    for times in range(1000):

        i3.left(angle)
    
        i3.circle(times * 10)
        i3.forward(43)

def pi2(i2):
    side = 8
    angle = 135
    distance = 100

    for times in range(1000):

        i2.left(angle)
    
        i2.circle(times * 10)
        i2.forward(43)

        i2.left(45)
        i2.forward(100)



def pi1(i1):
    side = 8
    angle = 135
    distance = 100

    for times in range(1000):

        i1.left(angle)
    
        i1.circle(times * 10)
        i1.forward(43)
    

        i1.left(45)
        i1.forward(100)

        i1.right(45)
        i1.forward(100)


def pi3t(i3):
    angle = 135
    distance = 43

    for times in range(255):
        c = (times * 1,0,times * 1)
        i3.color(c)
        i3.left(angle)    
        i3.circle(times * 10)
        i3.forward(distance)

    for times in range(127):
        c = (0,times * 2,times * 1)
        i3.color(c)
        i3.left(angle)    
        i3.circle(times * 10)
        i3.forward(distance)





def pi2t(i2):
    side = 8
    angle = 135
    distance = 100

    for times in range(255):
        c = (times * 1,0,times * 1)
        i2.color(c)
        i2.left(angle)
    
        i2.circle(times * 10)
        i2.forward(43)

        i2.left(45)
        i2.forward(100)



def pi1t(i1):
    side = 8
    angle = 135
    distance = 100

    for times in range(255):

        c = (0,times * 1,times * 1)
        i1.color(c)
        i1.left(angle)
    
        i1.circle(times * 10)
        i1.forward(43)
    

        i1.left(45)
        i1.forward(100)

        i1.right(45)
        i1.forward(100)



    for times in range(127):

        c = (times * 1,0,times * 1)
        i1.color(c)
        i1.left(angle)
    
        i1.circle(times * 10)
        i1.forward(43)
    

        i1.left(45)
        i1.forward(100)

        i1.right(45)
        i1.forward(100)

