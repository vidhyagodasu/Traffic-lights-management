import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
#images_folder = glob.glob("images/*.jpg")

vehicles_folder_count = 0
Elist=[]
images_folder1 = glob.glob("East/*.jpg")
for img_path1 in images_folder1:
    
    img = cv2.imread(img_path1)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
        
    Elist.append(vehicle_count)
    cv2.imshow("East", img)
    cv2.waitKey(1)
    
print("Total current count", vehicles_folder_count)
def roundof(x):
    if x>=0:
        return 0
    else :
        return abs(x)

def crossed(y,r):
    if y/r>= 30 :
        return 30*r
    else :
        return y

def newcrossed(k,ra,t):
    if k/ra>=t:
        return t*ra
    else :
        return k

def Green(z):
    if z >= 60*rate:
        return 60
    elif (z/rate)<10:
        return 10
    else :
        return int(z/rate)
#divide the rate with incoming vehicles number
#pass the entering vehicle to the function and divide the rate there
VehE=[36,35,41,42,37,39,45]
VehS=[20,21,18,17,23,22,19]
VehW=[33,35,37,42,38,39,40]
VehN=[9,8,12,7,7,14,13]

print("No. of vehicles that reached the junction at CYCLE 1:")
East=Elist[0]
South=Elist[1]
West=Elist[2]
North=Elist[3]

print("No of vehicles coming from East  : ",East)
print("No of vehicles coming from South : ",South)
print("No of vehicles coming from West  : ",West)
print("No of vehicles coming from North : ",North)

SurplusE=SurplusS=SurplusW=SurplusN=0
rate=1
timeE=timeS=timeW=timeN=30
while(1):
    k=int(input('''Press
1. To view the statistics
Any other key : Terminate'''))
    if(k==1):
        
        AvgE=int(sum(VehE)/len(VehE))
        AvgS=int(sum(VehS)/len(VehS))
        AvgW=int(sum(VehW)/len(VehW))
        AvgN=int(sum(VehN)/len(VehN))

        NewtimeE=Green(AvgE+SurplusE)
        NewtimeS=Green(AvgS+SurplusS)
        NewtimeW=Green(AvgW+SurplusW)
        NewtimeN=Green(AvgN+SurplusN)

        VehE.append(East)
        VehS.append(South)
        VehW.append(West)
        VehN.append(North)

        WSurplusE=roundof((timeE*rate)-East)
        WSurplusS=roundof((timeS*rate)-South)
        WSurplusW=roundof((timeW*rate)-West)
        WSurplusN=roundof((timeN*rate)-North)

        SurplusE=roundof((NewtimeE*rate)-East)
        SurplusS=roundof((NewtimeS*rate)-South)
        SurplusW=roundof((NewtimeW*rate)-West)
        SurplusN=roundof((NewtimeN*rate)-North)

        #rate=int(input("Enter the rate at which the vehicles are crossing the Green light : "))

        print('''No.of vehicles that               Vehicles that are waiting         
        crossed the Green light             after the green light                         
            without using     with using       without using     with using                 Time of
            the algorithm     the algorithm    the algorithm     the algorithm       RedLight 	 GreenLight''')

        print("East  = ",crossed(East,rate),"\t\t",newcrossed (East,rate,NewtimeE),"\t\t\t",WSurplusE,"\t\t",SurplusE,"\t\t",NewtimeS+NewtimeW+NewtimeN,"\t",NewtimeE)
        print("South = ",crossed(South,rate),"\t\t",newcrossed(South,rate,NewtimeS),"\t\t\t",WSurplusS,"\t\t",SurplusS,"\t\t",NewtimeE+NewtimeW+NewtimeN,"\t",NewtimeS)
        print("West  = ",crossed(West,rate),"\t\t",newcrossed(West,rate,NewtimeW),"\t\t\t",WSurplusW,"\t\t",SurplusW,"\t\t",NewtimeE+NewtimeS+NewtimeN,"\t",NewtimeW)
        print("North = ",crossed(North,rate),"\t\t",newcrossed(North,rate,NewtimeN),"\t\t\t",WSurplusN,"\t\t",SurplusN,"\t\t",NewtimeE+NewtimeS+NewtimeW,"\t",NewtimeN)
    else:
        break



    
    





