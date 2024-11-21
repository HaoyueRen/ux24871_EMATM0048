# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:51:12 2024

@author: Haoyue Ren

Set the initial fund of the hatchery to 10000.
If the operating funds are zero, assume bankruptcy.
By default, the recources in the main warehouse is preferentially used
unified words
simplify by loops

"""

#Define fixed cost each quarter
FixCost = 1500

#Define the Maximum number of hires.
MaximumHires = 5

#Define the inicial fund is 0.
Fund = 10000

#Define the inicial number of employees is 0
Num_employee=0

#Define the inicial warehouses status:
warehouse_status= {'Main warehouse': {'Fertilizer(litres)': 20 ,'Feed (kg)': 400 , 'Salt (kg)': 200 },
                  'Auxiliary Warehouse': {'Fertilizer(litres)': 10 ,'Feed (kg)': 200 , 'Salt (kg)': 100 },}

#Store the total quantities of various resources in one list.
resources={'Fertilizer(litres)': 30 ,'Feed (kg)': 600 , 'Salt (kg)': 300}

#Store the capacity of warehouses
Capacity= {'Main warehouse': {'Fertilizer(litres)': 20 ,'Feed (kg)': 400 , 'Salt (kg)': 200 },
                  'Auxiliary Warehouse': {'Fertilizer(litres)': 10 ,'Feed (kg)': 200 , 'Salt (kg)': 100 },}
ResourcesCapacity ={'Fertilizer(litres)': 30 ,'Feed (kg)': 600 , 'Salt (kg)': 300}


#Define the maintain cost of warehouses (unified unit)
warehouses_price = {'Fertilizer(litres)': 0.1 ,'Feed (kg)': 1 , 'Salt (kg)': 1 }

#Define the maintain cost of purchase (unified unit)
SlipperyLakes = {'Fertilizer(litres)': 0.3 ,'Feed (kg)': 0.1 , 'Salt (kg)': 0.05 }
ScalyWholesaler = {'Fertilizer(litres)': 0.2 ,'Feed (kg)': 0.4 , 'Salt (kg)': 0.25 }




#Define a list of employees with a maximum of five potential hires.
Employees_menu=['Employee1','Employee2','Employee3','Employee4','Employee5']

#Use a set to store information of fishes
fishes =  {'Clef Fins': {'Fertilizers (ml)': 100 ,'Feed (kg)': 12 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.0},
           'Timpani Snapper': {'Fertilizers (ml)': 50 ,'Feed (kg)': 9 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':1.0},
           'Andalusian Brim': {'Fertilizers (ml)': 90 ,'Feed (kg)': 6 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':0.5},
           'Plagal Cod': {'Fertilizers (ml)': 100 ,'Feed (kg)': 10 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.0},
           'Fugue Flounder': {'Fertilizers (ml)': 200 ,'Feed (kg)': 12 , 'Salt (kg)': 2 ,'Maintenance Time (in days)':2.5},
           'Modal Bass': {'Fertilizers (ml)': 300 ,'Feed (kg)': 12 , 'Salt (kg)': 6 ,'Maintenance Time (in days)':3},}



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


###########################################################################
#Define a function to manage the addition and removal of technicans
def HumanRecources(Num_employee0,Employee_menu0):
   x=0
   print("Would you like to adjust the staffing arrangement?")
   print('Current number of employees is '+ str(Num_employee0))
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
               elif Num_employee0+change>5:
                   print('The maximum number of employees is 5. Please choose again.')
               else:
                   
                   #Enter technican names
                   for i in list(range(1,int(change)+1)):
                       Employee_menu0[int(Num_employee0+i)-1]=input("Enter technician name:")
                       print("You hired "+Employee_menu0[int(Num_employee0+i)-1]+", weekly rate=" + str(WeeklyRate))
                       
                   #renew the number of employee  
                   Num_employee0=Num_employee0+change
                   
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
               elif Num_employee0+change<1:
                   print('You cannot have zero or a negative number of workers.')
               else:
                   
                   #need select which employee to be hired????????
                   #print("Current technican list:\n")
                   #for i in list(range(1,int(Num_employee0)+1)):
                    #   print(str(i)+', '+Employee_menu0[i])
                   #
                   #for i in list(range(1,int(change)+1)):
                    #   fired=input('Select the number in front of the name of the '+'No.'+str(i)+' employee you want to fire.')
                     #  print('You fired '+Employee_menu0[int(fired)-1]+'.')
                   
                   
                   #Mention the person fired
                   for i in list(range(1,int(change)+1)):
                       print("You fired "+Employee_menu0[int(Num_employee0)-i]+", weekly rate=" + str(WeeklyRate))
                       Employee_menu0[int(Num_employee0)-i]='Employee'+str(int(Num_employee0)-i+1)
                     
                   #renew the number of employee
                   Num_employee0=Num_employee0-change
                   break
                   x3+=1
                   x+=1
           
           break
       elif Choice=='C':
           x+=1
           break
    
   return Num_employee0,Employee_menu0


#Test block:
#HumanRecources(3,Employees_menu)
#Num_employee0=0
#Employees_menu=['Employee1','Employee2','Employee3','Employee4','Employee5']
#Employee_menu0=Employees_menu
#Employees_menu[4]
###########################################################################
#Define a function to calculate resources 
#test
#Num_employee0=Num_employee
#resources0=resources
#i = 'Clef Fins'


def CalculateResources(Num_employee0,resources0):
    #sell each fish in turn
    LabourInDays=Num_employee0*5*9
    
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
            if LabourInDays < float(fishes[i]['Maintenance Time (in days)']*quantity):
                print('Insufficient labour: required ' + str(fishes[i]['Maintenance Time (in days)']*quantity) + ' days, available ' + str(LabourInDays) + ' days. Please choose again.')
                continue
            #check fertilizer
            if resources0['Fertilizer(litres)']*1000 < float(fishes[i]['Fertilizers (ml)']*quantity):
                print("Insufficient fertilizers: required {0} litres, available {1} litres. Please choose again.".format(fishes[i]['Fertilizers (ml)']*quantity/1000, resources0['Fertilizer(litres)']))
                continue
            #check feed
            if resources0['Feed (kg)'] < float(fishes[i]['Feed (kg)']*quantity):
                print("Insufficient feed: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Feed (kg)']*quantity, resources0['Feed (kg)']))
                continue
            #check salt
            if resources0['Salt (kg)'] < float(fishes[i]['Salt (kg)']*quantity):
                print("Insufficient salt: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Salt (kg)']*quantity, resources0['Salt (kg)']))
                continue
            
            
            #Store the total consumption of various resources per quarter in another list
            consumption={'Fertilizer(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}
            
            #renew labor
            LabourInDays = LabourInDays - float(fishes[i]['Maintenance Time (in days)']*quantity)


            #calculate the consumption of recources
            consumption0['Fertilizer(litres)'] = fishes[i]['Fertilizers (ml)']*quantity/1000
            consumption0['Feed (kg)'] = fishes[i]['Feed (kg)']*quantity
            consumption0['Salt (kg)'] = fishes[i]['Salt (kg)']*quantity
            
            #renew total consumption
            Totalconsumption0['Fertilizer(litres)'] = Totalconsumption0['Fertilizer(litres)'] + fishes[i]['Fertilizers (ml)']*quantity/1000
            Totalconsumption0['Feed (kg)'] = Totalconsumption0['Feed (kg)'] + fishes[i]['Feed (kg)']*quantity
            Totalconsumption0['Salt (kg)'] = Totalconsumption0['Salt (kg)'] + fishes[i]['Salt (kg)']*quantity
        
            #Renew the current resources
            resources0['Fertilizer(litres)'] = resources0['Fertilizer(litres)'] - consumption0['Fertilizer(litres)']
            resources0['Feed (kg)'] = resources0['Feed (kg)'] - consumption0['Feed (kg)']
            resources0['Salt (kg)'] = resources0['Salt (kg)'] - consumption0['Salt (kg)']
            
        
            #summary then break
            print('Fish '+ i + ', demand ' + str(demands[i]['Demand']) + ', sell ' + str(quantity) + ' units.')
            InCome = InCome + quantity*demands[i]['Price']
            break
            
    return resources0, InCome,Totalconsumption0
       

###########################################################################
#Define a function to manage the warehouse status
def ManageWarehouse(consumption0,warehouse_status0):
    #loop over keys
    for i in consumption0.keys():
        if consumption0[i] >= warehouse_status0['Main warehouse'][i]:
            
            remain = consumption0[i] - warehouse_status0['Main warehouse'][i]
            #Rescouces in Main warehouse used up
            warehouse_status0['Main warehouse'][i]=0
            #then use from aux warehouse
            warehouse_status0['Auxiliary Warehouse'][i] =round(( warehouse_status0['Auxiliary Warehouse'][i] - remain),2)
        else:
            warehouse_status0['Main warehouse'][i]= round((warehouse_status0['Main warehouse'][i] - consumption0[i]),2)
            
    
    return warehouse_status0
        



###########################################################################
#Define a function to renew cash 
#Test
#Employees_menu0=Employees_menu
#Num_employee0=3
#i=3
#warehouse_status0=warehouse_status

def RenewCash(Num_employee0, Employees_menu0, InCome0, Fund, warehouse_status0):
    #add income from selling fishes
    Fund = Fund + InCome0
    
    #pay the salary
    for i in range(0,int(Num_employee0)):
        print('Paid ' + Employees_menu0[i] + ', weekly rate='+ str(WeeklyRate)+' amount ' + str(WeeklyRate*12))
        Fund = Fund - WeeklyRate*12
    
    #payfor warehouses
    WarehouseCost0 = 0
    #loop over resources
    for a in warehouse_status0.keys():
        for b in warehouse_status0[a].keys():
            cost0 = round(warehouses_price[b] * warehouse_status0[a][b], 2)
            Fund = Fund - cost0
            WarehouseCost0 = WarehouseCost0 + cost0
            print(a + ': ' + b + " cost " + str(cost0) + ' .')
        
    
    
    
    #pay the fixed cost
    Fund = Fund - FixCost
    print("Paid rent/utilities " + str(FixCost))
    
    return Fund
    


###########################################################################
#Test
#FromWhat=3
#a = 'Main warehouse'
#Capacity0 = Capacity0
resources0=resources
#Define a function to purchase supplies
def purchase(Fund0, resources0, warehouse_status0, Capacity0):
    print("List of Vendors \n    1. Slippery Lakes: Fertilizers £0.30/litre, Feed £0.10/g, Salt £0.05/g \n    2. Scaly Wholesaler: Fertilizers £0.20/litre, Feed £0.40/kg, Salt £0.25/kg")
     
    print("To fully replenish the pantry, you need purchase: ")
    print("Fertilizer: " + str(ResourcesCapacity['Fertilizer(litres)'] - resources0['Fertilizer(litres)']) + 'litres.')
    print("Feed: " + str(ResourcesCapacity['Feed (kg)'] - resources0['Feed (kg)']) + 'kg.')
    print("Salt: " + str(ResourcesCapacity['Salt (kg)'] - resources0['Salt (kg)']) + 'kg.')
    
    
    initialfund = Fund0
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
           #calculate supply of each resources
           for a in SlipperyLakes.keys():
                   Cost0 = SlipperyLakes[a] * (ResourcesCapacity[a] - resources0[a])
                   
                   Fund0 = Fund0 - Cost0
                   TotalPrice = TotalPrice + Cost0
                   if Fund0 <0 :
                       print("Can't restock "+ a +", insufficient funds, need " + str(Cost0) + " but only have" + str(initialfund)) 
                       break
                   resources0[a] = resources0[a] + (ResourcesCapacity[a] - resources0[a])
                   warehouse_status0['Main warehouse'][a] = Capacity['Main warehouse'][a]
                   warehouse_status0['Auxiliary Warehouse'][a] = Capacity['Auxiliary Warehouse'][a]
            
           break
        if FromWhat == 2.0: 
           #chosen Scaly Wholesaler
           #calculate supply of each resources
           for a in ScalyWholesaler.keys():
                   Cost0 = ScalyWholesaler[a] * (ResourcesCapacity[a] - resources0[a])
                   initialfund = Fund0
                   Fund0 = Fund0 - Cost0
                   TotalPrice = TotalPrice + Cost0
                   if Fund0 <0 :
                       print("Can't restock "+ a +", insufficient funds, need " + str(Cost0) + " but only have" + str(initialfund)) 
                       break
                   resources0[a] = resources0[a] + (ResourcesCapacity[a] - resources0[a])
                   warehouse_status0['Main warehouse'][a] = Capacity['Main warehouse'][a]
                   warehouse_status0['Auxiliary Warehouse'][a] = Capacity['Auxiliary Warehouse'][a]
                       
                 
           break
        
        
        
        
        
        
    return Fund0, resources0, warehouse_status0, TotalPrice,initialfund





            
                
###########################################################################
#The main function
#i=1
#Test
Num_employee1=Num_employee
Employee_menu1=Employees_menu
resources1 = resources
warehouse_status1=warehouse_status
Fund1 = Fund



def Hatchery(Num_employee1, Employee_menu1,warehouse_status1,Fund1, resources1):

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
        TechnicansManagement = HumanRecources(Num_employee1,Employee_menu1)
        #renew 
        Num_employee1 = TechnicansManagement[0]
        Employee_menu1 = TechnicansManagement[1]
        
        #start sell fishes, renew list of recources and get income 
        CalculateResult = CalculateResources(Num_employee1,resources1)
        resources1 = CalculateResult[0]
        InCome1 = CalculateResult[1]
        Totalconsumption1 = CalculateResult[2]
        
        #calculate and renew the fund
        warehouse_status1 = ManageWarehouse(Totalconsumption1,warehouse_status1)
        
        #calculate and renew the fund
        Fund1 = RenewCash(Num_employee1, Employee_menu1, InCome1, Fund1, warehouse_status1)
        
        #check if bankrupted
        
        #Depreciation
        for a in warehouse_status1.keys():
            for b in warehouse_status1[a].keys():
                 warehouse_status1[a][b] = int(warehouse_status1[a][b] *(1-Depreciation[b]))
         
        #renew the resource   
        for c in resources1.keys():
            resources1[c] = warehouse_status1['Main warehouse'][c] + warehouse_status1['Auxiliary Warehouse'][c]
         
        
        #purchase
        AfterPurchase = purchase(Fund1, resources1, warehouse_status1, Capacity)
        Fund1=AfterPurchase[0]
        TotalPrice = AfterPurchase[3]
        InitialFund1 = AfterPurchase[4]
        
        if Fund1 <0:
            print("Went bankrupt restocking warehouse Main in quarter" + str(j))

            break
        
        resources1=AfterPurchase[1]
        warehouse_status1=AfterPurchase[2]
        
        
        #report and summary
        print("Hatchery Name: Eastaboga, Cash: " + str(Fund1))
        for a in warehouse_status1.keys():
            print(a + ':')
            for b in warehouse_status1[a].keys():
                 print(b + ': ' + str(warehouse_status1[a][b]) + "(Capacity = " + str(Capacity[a][b]) + ' )')
        
        for t in list(range(0,int(Num_employee1))):
            print('Technician ' + Employee_menu1[1] + ' , weekly rate = ' + str(WeeklyRate) + '.')
        
                 
        
                 
        print("END OF QUARTER " + str(j))
    
    
Hatchery(Num_employee, Employees_menu,warehouse_status,Fund, resources)
    
25*250+3500+15*250
0.3*4.35+480*0.1+100*0.05
