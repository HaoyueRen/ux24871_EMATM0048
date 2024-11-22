# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:51:12 2024

@author: Haoyue Ren

Set the initial fund of the hatchery to 10000.
If the operating funds are zero, assume bankruptcy.
By default, the recources in the main warehouse is preferentially used
unified words
simplify by loops
Added a preview of the breedable quantity.

build the class
simplify
"""

###########################################################################

#Define fixed cost each quarter
FixCost = 1500

#Define the Maximum number of hires.
MaximumHires = 5


#Define the inicial number of employees is 0
Num_employee=0

#Some Fix coefficients
#Store the capacity of warehouses
Capacity= {'Main warehouse': {'Fertilizer(litres)': 20 ,'Feed (kg)': 400 , 'Salt (kg)': 200 },
                  'Auxiliary Warehouse': {'Fertilizer(litres)': 10 ,'Feed (kg)': 200 , 'Salt (kg)': 100 },}
ResourcesCapacity ={'Fertilizer(litres)': 30 ,'Feed (kg)': 600 , 'Salt (kg)': 300}

#Define the maintain cost of warehouses (unified unit)
warehouses_price = {'Fertilizer(litres)': 0.1 ,'Feed (kg)': 1 , 'Salt (kg)': 1 }

#Define the maintain cost of purchase (unified unit)
SlipperyLakes = {'Fertilizer(litres)': 0.3 ,'Feed (kg)': 0.1 , 'Salt (kg)': 0.05 }
ScalyWholesaler = {'Fertilizer(litres)': 0.2 ,'Feed (kg)': 0.4 , 'Salt (kg)': 0.25 }

#Use a set to store information of fishes(unified unit)
fishes =  {'Clef Fins': {'Fertilizer(litres)': 0.1 ,'Feed (kg)': 12 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.0},
           'Timpani Snapper': {'Fertilizer(litres)': 0.05 ,'Feed (kg)': 9 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':1.0},
           'Andalusian Brim': {'Fertilizer(litres)': 0.09 ,'Feed (kg)': 6 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':0.5},
           'Plagal Cod': {'Fertilizer(litres)': 0.1 ,'Feed (kg)': 10 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.0},
           'Fugue Flounder': {'Fertilizer(litres)': 0.2 ,'Feed (kg)': 12 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.5},
           'Modal Bass': {'Fertilizer(litres)': 0.3 ,'Feed (kg)': 12 , 'Salt (kg)': 6 ,'Maintenance Time (in days)':3},}


#To store information of demands and prices
demands =  {'Clef Fins': {'Demand': 25 ,'Price': 250 },
           'Timpani Snapper': {'Demand': 10 ,'Price': 350 },
           'Andalusian Brim': {'Demand': 15 ,'Price': 250 },
           'Plagal Cod': {'Demand': 20 ,'Price': 400 },
           'Fugue Flounder': {'Demand': 30 ,'Price': 550 },
           'Modal Bass': {'Demand': 50 ,'Price': 500 },}

#Define weekly rate of technicans
WeeklyRate = 500

#rate of depreciation
Depreciation = {'Fertilizer(litres)': 0.4 ,'Feed (kg)': 0.1 , 'Salt (kg)': 0 }

#create a list to store the order of fishes
FishOrder={1:'Clef Fins', 2:'Timpani Snapper', 3:'Andalusian Brim', 4: 'Plagal Cod', 5:'Fugue Flounder', 6: 'Modal Bass', 7: 'Common'}

###########################################################################


class Hatchery:
    def __init__(self, warehouse_status, resources,Employee_menu,Num_employee,Fund,Labour_Distribute,Speciality):
        
        #store the warehouses status
        self.warehouse_status = warehouse_status
        
        #the total quantities of various resources in one list.
        self.resources = resources
        
        #Define a list of employees with a maximum of five potential hires.
        self.Employee_menu = Employee_menu
        
        #Define the number of employees with a maximum of five potential hires.
        self.Num_employee = Num_employee
        
        #Define the fund status
        self.Fund = Fund
        #Define the distribute of different special
        self.Labour_Distribute = Labour_Distribute
        
        #Store their speciality
        self.Speciality = Speciality
        
        
        
    def introduceTechnicans(self):
        for t in list(range(1,int(self.Num_employee)+1)):
            print(str(t)+', '+self.Employee_menu[t-1] + ', specializes in work about ' + self.Speciality[self.Employee_menu[t-1]] + ' fish. weekly rate = ' + str(WeeklyRate) + '. ')
    

###########################################################################
#Define a initial hatchery
hatchery1 = Hatchery(
    #Define the inicial warehouses status:
warehouse_status= {'Main warehouse': {'Fertilizer(litres)': 20 ,'Feed (kg)': 400 , 'Salt (kg)': 200 },
                  'Auxiliary Warehouse': {'Fertilizer(litres)': 10 ,'Feed (kg)': 200 , 'Salt (kg)': 100 },}, 
#Store the total quantities of various resources in one list.
resources={'Fertilizer(litres)': 30 ,'Feed (kg)': 600 , 'Salt (kg)': 300},
#Define a list of employees with a maximum of five potential hires.
Employee_menu=['Empty','Empty','Empty','Empty','Empty'],
Num_employee = 0,
#Define a list to represent different types of labor 
Labour_Distribute = {'Clef Fins':0 ,'Timpani Snapper':0 ,'Andalusian Brim':0 ,'Plagal Cod':0 ,'Fugue Flounder':0 ,'Modal Bass':0,'Common':0 },
#Define the inicial fund is 0.
Fund = 10000,
#initialize their speciality, not hire now.
Speciality ={}
)
    
#Test
hatchery0 = hatchery1
    

###########################################################################
#Define a function to manage the addition and removal of technicans
def HumanRecources(hatchery0):
   x=0
   print("Would you like to adjust the staffing arrangement?")
   print('Current number of employees is '+ str(hatchery0.Num_employee))
   hatchery0.introduceTechnicans()
   #loop until input correctly
   while x<1:
       Choice= input("A, hire new employees\nB, fire employees.\nC, no change.")
       if (Choice in ['A','B','C'])==False:
           print('Please enter a valid option.')
       elif Choice=='A':
           #when hiring
           x2=0
           while x2<1:
               
               change=input('Please enter the number of hires. ')
               try:
                   change=float(change)
               except ValueError:
                   print("Please enter an integer.")
                   continue
               if (change%1)!=0:
                   print('Please enter an integer.')
               elif hatchery0.Num_employee+change>5:
                   print('The maximum number of employees is 5. Please choose again.')
               else:
                   
                   #Enter technican names
                   for i in list(range(1,int(change)+1)):
                       
                       #loop until valid input
                       while True:
                           Whether = input("Do you want to hire a technician with a specialty?\nA,Yes\nB,No")
                           if (Whether!='A')&(Whether!='B'):
                               print('Please enter a valid option.')
                               continue
                           if Whether=='A':
                               while True:
                                   specialty=input("Select the fish type this technican specialise in: \n1, Clef Fins\n2, Timpani Snapper\n3, Andalusian Brim\n4, Plagal Cod\n5, Fugue Flounder\n6, Modal Bass")
                                   try:
                                       specialty=float(specialty)
                                   except ValueError:
                                       print("Please enter an integer.")
                                       continue
                                   if specialty%1!=0:
                                       print("Please enter an integer.")
                                       continue
                                   if specialty<=0:
                                       print("Please enter a positive non-zero number.")
                                       continue
                                   if specialty>6:
                                       print("Please select in correct range.")
                                       continue
                                   
                                   #add the labour days in the specialised field
                                   hatchery0.Labour_Distribute[FishOrder[specialty]] = hatchery0.Labour_Distribute[FishOrder[specialty]] + 1
                                   
                                   #enter the worker neme and label the specialty
                                   hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]=input("Enter technician name:")
                                   print("You hired "+hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]+", weekly rate=" + str(WeeklyRate))
                                   
                                   #store their speciality
                                   hatchery0.Speciality[hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]] = FishOrder[specialty]
                                   break
                               break
                                   
                                   
                                   
                           elif Whether=='B':
                               hatchery0.Labour_Distribute['Common'] = hatchery0.Labour_Distribute['Common'] + 1
                               hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]=input("Enter technician name:")
                               print("You hired "+hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]+", weekly rate=" + str(WeeklyRate))
                               
                               #store their speciality,marked as common
                               hatchery0.Speciality[hatchery0.Employee_menu[int(hatchery0.Num_employee+i)-1]] = FishOrder[7]
                               
                               
                               break
                      
                       
                   #renew the number of employee  
                   hatchery0.Num_employee = hatchery0.Num_employee + change
                   
                   break
                   x2+=1
                   x+=1
           break
       
       elif Choice=='B':
           #when firing
           x3=0
           while x3<1:
               
               change=input('Please enter the number of fires. ')
               try:
                   change=float(change)
               except ValueError:
                   print("Please enter an integer.")
                   continue
               if (change%1)!=0:
                   print('Please enter an integer.')
               elif hatchery0.Num_employee - change<1:
                   print('You cannot have zero or a negative number of workers.')
                   continue
               else:
                   
                   #select which employee to be hired
                   hatchery0.introduceTechnicans()
                   for i in list(range(1,int(change)+1)):
                       #loop until valid input
                       while True:
                           fired=input('Select the number in front of the name of the '+'No.'+str(i)+' employee you want to fire.')
                           try:
                               fired=float(fired)
                           except ValueError:
                               print("Please enter an integer.")
                               continue
                           if fired%1!=0:
                               print("Please enter an integer.")
                               continue
                           if fired<=0:
                               print("Please enter a positive non-zero number.")
                               continue
                           if fired>hatchery0.Num_employee:
                               print("Please select in correct range.")
                               continue
                           break
                       #renew the babour distribution
                       RemovedLabour = hatchery0.Speciality[hatchery0.Employee_menu[int(fired)-1]]
                       hatchery0.Labour_Distribute[RemovedLabour] = hatchery0.Labour_Distribute[RemovedLabour] - 1
                       
                       #delete the person from speciality dictionary and  employee menu
                       keytoremove = list(hatchery0.Speciality.keys())[int(fired)-1]
                       hatchery0.Employee_menu.remove(keytoremove)
                       hatchery0.Employee_menu.insert(4, 'Empty')
                       print('You fired '+keytoremove+", weekly rate=" + str(WeeklyRate)+'.')
                   
                     
                        
                   #renew the number of employee
                   hatchery0.Num_employee = hatchery0.Num_employee-change
                   break
                   x3+=1
                   x+=1
           
           break
       elif Choice=='C':
           x+=1
           break
    
   return hatchery0


###########################################################################
#Define maximum supply


def MaximumSupply(LabourInDays2,resources2,Index):
    #print rescouces to check
    print("Remaining available labor time: " + str(LabourInDays2) + "days.")
    print("Available Resources: " )
    for x in resources2.keys():
        print(x + ": " +str(resources2[x]))
    #calculate the maximum supply from each resource
    maximumValues = [int(LabourInDays2/fishes[Index]['Maintenance Time (in days)'])]
    for y in resources2.keys():
        maximumValues.append(int(resources2[y]/fishes[Index][y]))
    #calculate the ultimate maximum supply
    Maximum = min(maximumValues)
    print("The maximum "+Index+" quantity that can be produced is : " + str(Maximum))




###########################################################################
#Define a function to calculate resources 
#test
#Num_employee0=Num_employee
#resources0=resources
#i = 'Clef Fins'


def CalculateResources(hatchery0):
    #calculate lobour days by speciality
    LabourInDays = {}
    for d in hatchery0.Labour_Distribute.keys():
        LabourInDays[d] = 6*5*hatchery0.Labour_Distribute[d]
        
    #Aside from the specialized work days, each employee has three weeks of general fish-related work time.
    LabourInDays['Common'] = LabourInDays['Common'] + hatchery0.Num_employee*3*5
    
    
    
    consumption0={'Fertilizer(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}
    Totalconsumption0={'Fertilizer(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}
    InCome = 0
    for i in demands.keys():
        #each technician provides nine weeks of labour per quarter
        #LabourInDays=LabourInDays-fishes[i]['Maintenance Time (in days)']*demands[i]['Demand']
        #within the limits of available labor
        
        #loop until valid input
        while True:
            quantity = input('How many units of '+ i +' would you like to sell?\nDeamnd of '+i+' is '+str(demands[i]['Demand'])+' units.')
            try:
                quantity=float(quantity)
            except ValueError:
                print("Please enter a number.")
                continue
            if quantity < 0:
                print("Please enter a positive number.")
                continue
        
            
            #check if in the correct range
            #check demand
            if quantity > demands[i]['Demand']:
                print("Please do not exceed the maximum demand"+str(demands[i]['Demand'])+' units.' )
                continue
            #check labour
            if (LabourInDays[i]+LabourInDays['Common']) < float(fishes[i]['Maintenance Time (in days)']*quantity):
                print('Insufficient labour: required ' + str(fishes[i]['Maintenance Time (in days)']*quantity) + ' days, available ' + str((LabourInDays[i]+LabourInDays['Common'])) + ' days. Please choose again.')
                MaximumSupply((LabourInDays[i]+LabourInDays['Common']),hatchery0.resources,i)
                continue
            
            #check fertilizer
            if hatchery0.resources['Fertilizer(litres)']< float(fishes[i]['Fertilizer(litres)']*quantity):
                print("Insufficient fertilizers: required {0} litres, available {1} litres. Please choose again.".format(fishes[i]['Fertilizer(litres)']*quantity, hatchery0.resources['Fertilizer(litres)']))
                MaximumSupply((LabourInDays[i]+LabourInDays['Common']),hatchery0.resources,i)
                continue
            #check feed
            if hatchery0.resources['Feed (kg)'] < float(fishes[i]['Feed (kg)']*quantity):
                print("Insufficient feed: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Feed (kg)']*quantity, hatchery0.resources['Feed (kg)']))
                MaximumSupply((LabourInDays[i]+LabourInDays['Common']),hatchery0.resources,i)
                continue
            #check salt
            if hatchery0.resources['Salt (kg)'] < float(fishes[i]['Salt (kg)']*quantity):
                print("Insufficient salt: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Salt (kg)']*quantity, hatchery0.resources['Salt (kg)']))
                MaximumSupply((LabourInDays[i]+LabourInDays['Common']),hatchery0.resources,i)
                continue
            
            
            #Store the total consumption of various resources per quarter in another list
            consumption={'Fertilizer(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}
            
            #renew labor
            #Prioritize the use of specialized work days.
            #Use common work days when specialized work days are insufficient.
            if LabourInDays[i]<float(fishes[i]['Maintenance Time (in days)']*quantity):
                remainingdays = float(fishes[i]['Maintenance Time (in days)']*quantity) - LabourInDays[i]
                LabourInDays[i] = 0
                LabourInDays['Common'] = LabourInDays['Common'] - remainingdays
            else:
                LabourInDays[i] = LabourInDays[i] -float(fishes[i]['Maintenance Time (in days)']*quantity)
                
      
            #calculate the consumption of recources
            consumption0['Fertilizer(litres)'] = fishes[i]['Fertilizer(litres)']*quantity
            consumption0['Feed (kg)'] = fishes[i]['Feed (kg)']*quantity
            consumption0['Salt (kg)'] = fishes[i]['Salt (kg)']*quantity
            
            #renew total consumption
            Totalconsumption0['Fertilizer(litres)'] = Totalconsumption0['Fertilizer(litres)'] + fishes[i]['Fertilizer(litres)']*quantity
            Totalconsumption0['Feed (kg)'] = Totalconsumption0['Feed (kg)'] + fishes[i]['Feed (kg)']*quantity
            Totalconsumption0['Salt (kg)'] = Totalconsumption0['Salt (kg)'] + fishes[i]['Salt (kg)']*quantity
        
            #Renew the current resources
            hatchery0.resources['Fertilizer(litres)'] = hatchery0.resources['Fertilizer(litres)'] - consumption0['Fertilizer(litres)']
            hatchery0.resources['Feed (kg)'] = hatchery0.resources['Feed (kg)'] - consumption0['Feed (kg)']
            hatchery0.resources['Salt (kg)'] = hatchery0.resources['Salt (kg)'] - consumption0['Salt (kg)']
            
        
            #summary then break
            print('Fish '+ i + ', demand ' + str(demands[i]['Demand']) + ', sell ' + str(quantity) + ' units.')
            InCome = InCome + quantity*demands[i]['Price']
            break
            
    return hatchery0, InCome,Totalconsumption0
       

###########################################################################
#Define a function to manage the warehouse status
def ManageWarehouse(consumption0,hatchery0):
    #loop over keys
    for i in consumption0.keys():
        if consumption0[i] >= hatchery0.warehouse_status['Main warehouse'][i]:
            
            remain = consumption0[i] - hatchery0.warehouse_status['Main warehouse'][i]
            #Rescouces in Main warehouse used up
            hatchery0.warehouse_status['Main warehouse'][i]=0
            #then use from aux warehouse
            hatchery0.warehouse_status['Auxiliary Warehouse'][i] =round(( hatchery0.warehouse_status['Auxiliary Warehouse'][i] - remain),2)
        else:
            hatchery0.warehouse_status['Main warehouse'][i]= round((hatchery0.warehouse_status['Main warehouse'][i] - consumption0[i]),2)
            
    
    return hatchery0
        



###########################################################################
#Define a function to renew cash 
#Test
#Employees_menu0=Employees_menu
#Num_employee0=3
#i=3
#warehouse_status0=warehouse_status

def RenewCash(hatchery0, InCome0 ):
    #add income from selling fishes
    hatchery0.Fund = hatchery0.Fund + InCome0
    
    #pay the salary
    for i in range(0,int(hatchery0.Num_employee)):
        print('Paid ' + hatchery0.Employee_menu[i] + ', weekly rate='+ str(WeeklyRate)+' amount ' + str(WeeklyRate*12))
        hatchery0.Fund = hatchery0.Fund - WeeklyRate*12
    
    #payfor warehouses
    WarehouseCost0 = 0
    
    
    #loop over resources
    for a in hatchery0.warehouse_status.keys():
        for b in hatchery0.warehouse_status[a].keys():
            cost0 = round(warehouses_price[b] * hatchery0.warehouse_status[a][b], 2)
            hatchery0.Fund = hatchery0.Fund - cost0
            WarehouseCost0 = WarehouseCost0 + cost0
            print(a + ': ' + b + " cost " + str(cost0) + ' .')
        
    
    
    
    #pay the fixed cost
    hatchery0.Fund = hatchery0.Fund - FixCost
    print("Paid rent/utilities " + str(FixCost))
    
    return hatchery0
    


###########################################################################

def purchase(hatchery0):
    print("List of Vendors \n    1. Slippery Lakes: Fertilizers £0.30/litre, Feed £0.10/g, Salt £0.05/g \n    2. Scaly Wholesaler: Fertilizers £0.20/litre, Feed £0.40/kg, Salt £0.25/kg")
     
    print("To fully replenish the pantry, you need purchase: ")
    print("Fertilizer: " + str(ResourcesCapacity['Fertilizer(litres)'] - hatchery0.resources['Fertilizer(litres)']) + 'litres.')
    print("Feed: " + str(ResourcesCapacity['Feed (kg)'] - hatchery0.resources['Feed (kg)']) + 'kg.')
    print("Salt: " + str(ResourcesCapacity['Salt (kg)'] - hatchery0.resources['Salt (kg)']) + 'kg.')
    
    
    initialfund = hatchery0.Fund
    #loop until valid input
    while True:
        FromWhat = input("Enter number of vendor to purchase from: ")
        try:
            FromWhat=float(FromWhat)
        except ValueError:
            print("Please enter a number.")
            continue
        if FromWhat < 0:
            print("Please enter a positive number.")
            continue
        #check if integer
        if FromWhat%1!= 0:
            print("Please enter an integer.")
            continue
    
        
        #check if in the correct range
        if (FromWhat != 1.0)&(FromWhat != 2.0):
            print("Please select over the two options! ")
            continue
        #Initialize a vairable to store total cost
        TotalPrice = 0
        if FromWhat == 1.0: 
           #chosen Scaly Wholesaler
           #calculate supply of each resources in both warehouses
           for d in hatchery0.warehouse_status.keys():
               for a in SlipperyLakes.keys():
                       Cost0 = SlipperyLakes[a] * (Capacity[d][a] - hatchery0.warehouse_status[d][a])
                       
                       hatchery0.Fund = hatchery0.Fund - Cost0
                       TotalPrice = TotalPrice + Cost0
                       if hatchery0.Fund <0 :
                           print("Can't restock "+ a +", insufficient funds, need " + str(Cost0) + " but only have" + str(initialfund)) 
                           break
                       hatchery0.resources[a] = hatchery0.resources[a] + (ResourcesCapacity[a] - hatchery0.resources[a])
                       hatchery0.warehouse_status[d][a] = Capacity[d][a]
            
           break
        if FromWhat == 2.0: 
           #chosen Scaly Wholesaler
           #calculate supply of each resources
           for a in ScalyWholesaler.keys():
                   Cost0 = ScalyWholesaler[a] * (ResourcesCapacity[a] - hatchery0.resources[a])
                   initialfund = hatchery0.Fund
                   hatchery0.Fund = hatchery0.Fund - Cost0
                   TotalPrice = TotalPrice + Cost0
                   if hatchery0.Fund <0 :
                       print("Can't restock "+ a +", insufficient funds, need " + str(Cost0) + " but only have" + str(initialfund)) 
                       break
                   hatchery0.resources[a] = hatchery0.resources[a] + (ResourcesCapacity[a] - hatchery0.resources[a])
                   hatchery0.warehouse_status['Main warehouse'][a] = Capacity['Main warehouse'][a]
                   hatchery0.warehouse_status['Auxiliary Warehouse'][a] = Capacity['Auxiliary Warehouse'][a]
                       
                 
           break
        
        
        
        
        
        
    return hatchery0, TotalPrice,initialfund





            
                
###########################################################################

def Main(hatchery0):

    Quarter = input("Enter the number of quarters to run the simulation(please enter a positive integer): ")
    try:
        Quarter=float(Quarter)
    except ValueError:
        print("Failed to enter valid input, will run as default:  run the simulation for 8 quarters.")
        Quarter= 8
        
    if Quarter < 0:
        print("Failed to enter valid input, will run as default:  run the simulation for 8 quarters.")
        Quarter= 8
        
    if Quarter%1 != 0:
        print("Failed to enter valid input, will run as default:  run the simulation for 8 quarters.")
        Quarter= 8
        
        

    for j in list(range(1,int(Quarter)+1)):
        #title
        print("================================ \n====== SIMULATING quarter " + str(j)+" ======\n================================ ")
        
        #manage technicans
        hatchery0 = HumanRecources(hatchery0)
        
        #start sell fishes, renew list of recources and get income 
        CalculateResult = CalculateResources(hatchery0)
        hatchery0 = CalculateResult[0]
        InCome1 = CalculateResult[1]
        Totalconsumption1 = CalculateResult[2]
        
        #calculate and renew the fund
        hatchery0 = ManageWarehouse(Totalconsumption1,hatchery0)
        
        #calculate and renew the fund
        hatchery0 = RenewCash(hatchery0, InCome1)
        
        #check if bankrupted
        
        #Depreciation
        for a in hatchery0.warehouse_status.keys():
            for b in hatchery0.warehouse_status[a].keys():
                hatchery0.warehouse_status[a][b] = int(hatchery0.warehouse_status[a][b] *(1-Depreciation[b]))
         
        #renew the resource   
        for c in hatchery0.resources.keys():
            hatchery0.resources[c] = hatchery0.warehouse_status['Main warehouse'][c] + hatchery0.warehouse_status['Auxiliary Warehouse'][c]
         
        
        #purchase
        AfterPurchase = purchase(hatchery0)
        hatchery0=AfterPurchase[0]
        TotalPrice = AfterPurchase[1]
        InitialFund1 = AfterPurchase[2]
        
        if hatchery0.Fund <0:
            print("Went bankrupt restocking warehouse Main in quarter" + str(j))

            break
        
      
        #report and summary
        print("Hatchery Name: Eastaboga, Cash: " + str(hatchery0.Fund))
        for a in hatchery0.warehouse_status.keys():
            print(a + ':')
            for b in hatchery0.warehouse_status[a].keys():
                 print(b + ': ' + str(hatchery0.warehouse_status[a][b]) + "(Capacity = " + str(Capacity[a][b]) + ' )')
        
        for t in list(range(0,int(hatchery0.Num_employee))):
            print('Technician ' + hatchery0.Employee_menu[1] + ' , weekly rate = ' + str(WeeklyRate) + '.')
        
                 
        
                 
        print("END OF QUARTER " + str(j))
    
    
Main(hatchery1)
    
25*250+3500+15*250
0.3*4.35+480*0.1+100*0.05
