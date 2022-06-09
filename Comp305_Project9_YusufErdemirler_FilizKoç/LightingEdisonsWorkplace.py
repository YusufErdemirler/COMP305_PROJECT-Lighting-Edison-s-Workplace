import time

#Start timing
st = time.time()

Area = []

#Get input data along with populating Array 2-D
with open("test4.txt","r") as f:
    count = 0
    for line in f:
        if count == 0:
            Row, Column, Radius = map(int, line.strip().split(" "))
            L = 2*Radius+1
        elif count == 1:
            CostCable, CostBulb, Budget = map(int, line.strip().split(" "))
        elif count == 2:
            x, y = map(int, line.strip().split(" "))
        else:
            Area.append(line.strip())
        count += 1
    
#Count number of area lit by placing bulb in x-y coordinate
def getLightedRoom(x, y, R, Area):
    lighted = 0
    
    AreaXLength = len(Area)-1
    AreaYLength = len(Area[0])-1
    
    #Constraints for border placement
    if x - R > 0 and y - R > 0 and x + R < AreaXLength and y + R < AreaYLength:
        for i in range(2*R + 1):
            for j in range(2*R + 1):
                if Area[x - R + i][y - R + j] == ".":
                    lighted += 1
                    
    elif x - R < 0 and y - R > 0 and y + R < AreaYLength:
        for i in range(x + R + 1):
            for j in range(2*R + 1):
                if Area[i][y - R + j] == ".":
                    lighted += 1
                    
    elif x - R > 0 and y - R < 0 and x + R < AreaXLength:
        for i in range(2*R + 1):
            for j in range(y + R + 1):
                if Area[x - R + i][j] == ".":
                    lighted += 1
                    
    elif x - R < 0 and y - R < 0:
        for i in range(x + R + 1):
            for j in range(y + R + 1):
                if Area[i][j] == ".":
                    lighted += 1
    
    elif x + R > AreaXLength and y + R < AreaYLength and y - R > 0:
       for i in range(AreaXLength - x + R + 1):
           for j in range(2*R + 1):
               if Area[x - R + i][y - R + j] == ".":
                   lighted += 1
                    
    elif x + R < AreaXLength and y + R > AreaYLength and x - R > 0:
        for i in range(2*R + 1):
            for j in range(AreaYLength - y + R + 1):
                if Area[x - R + i][y - R + j] == ".":
                    lighted += 1
                    
    elif x + R > AreaXLength and y + R > AreaYLength:
        for i in range(AreaXLength - x + R + 1):
            for j in range(AreaYLength - y + R + 1):
                if Area[x - R + i][y - R + j] == ".":
                    lighted += 1
                    
    elif x - R < 0 and y + R < AreaYLength:
        for i in range(x + R + 1):
            for j in range(2*R + 1):
                if Area[i][y - R + j] == ".":
                    lighted += 1
                    
    elif x - R > 0 and y + R > AreaYLength:
         for i in range(2*R + 1):
             for j in range(AreaYLength - y + R + 1):
                if Area[x - R + i][y - R + j] == ".":
                    lighted += 1
    
    elif x - R < 0 and y + R > AreaYLength:
        for i in range(x + R + 1):
            for j in range(AreaYLength - y + R + 1):
                if Area[i][y - R + j] == ".":
                    lighted += 1
                    
    elif x + R < AreaXLength and y - R < 0:
        for i in range(2*R + 1):
             for j in range(y + R + 1):
                if Area[x - R + i][j] == ".":
                    lighted += 1  
        
    elif x + R > AreaXLength and y - R > 0:
        for i in range(AreaXLength - x + R + 1):
            for j in range(y + R + 1):
                if Area[x - R + i][y - R + j] == ".":
                    lighted += 1
            
    elif x + R > AreaXLength and y - R < 0:
        for i in range(AreaXLength - x + R + 1):
            for j in range(y + R + 1):
                if Area[x - R + i][j] == ".":
                    lighted += 1
    
    #Make sure that the bulb itself isn't counted
    if Area[x][y] == ".":
        return lighted-1
    else:
        return lighted

#Count number of "." in an Area
def countLightable(Area):
    count = 0
    for i in Area:
        for j in i:
            if j == ".":
                count += 1
    return count

#Maximum number of bulbs that can be placed to light the whole Area
MaxLight = round(countLightable(Area) / (L*L))

i,j = 0,0
CurrCost = 0
totalLighted = 0
BulbCount = 0

#Greedy traversal of whole Area
while i < Row:
    while j < Column:
        #Make sure the area needs to be lit and that bulbcount isn't over max
        if Area[i][j] != "-" and BulbCount < MaxLight:
            lighted = getLightedRoom(i, j, Radius, Area)
            #Get the cost of placing bulb and make sure it isn't over budget
            lightCost = CostBulb + (abs(x-i)*CostCable + abs(y-j)*CostCable)
            if CurrCost+lightCost < Budget:
                CurrCost += lightCost 
                BulbCount += 1
                totalLighted += lighted
                #Go to another location that isn't lit by this placed bulb
                i += Radius
                j += Radius
            if j > Column or i > Row: 
                break
        j += 1
    i += 1
    j = 0
    
#Calculate run time of whole script
et = time.time()

print("Area lit:",totalLighted)
print('Execution time:', et - st, 'seconds')
