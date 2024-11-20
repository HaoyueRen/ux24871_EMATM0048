# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:51:12 2024

@author: Haoyue Ren

Set the initial fund of the hatchery to 10000.
If the operating funds are zero, assume bankruptcy.
"""
#Define the Maximum number of hires.
MaximumHires = 5

#Define the inicial fund is 0.
Fund = 10000

#Define the inicial number of employees is 0
Num_employee=0

#Define the inicial warehouses status:
warehouse_status= {'Main warehouse': {'Fertiliser(litres)': 20 ,'Feed (kg)': 400 , 'Salt (kg)': 200 },
                  'Auxiliary Warehouse': {'Fertilizers (litres)': 10 ,'Feed (kg)': 200 , 'Salt (kg)': 100 },}
#Define the maintain cost of warehouses
warehouses_price = {'Fertiliser(litres)': 0.1 ,'Feed (g)': 0.001 , 'Salt (g)': 0.001 }



#Store the total quantities of various resources in one list.
resources={'Fertiliser(litres)': 30 ,'Feed (kg)': 600 , 'Salt (kg)': 300}

#Store the total consumption of various resources per quarter in another list
consumption={'Fertiliser(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}

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


###########################################################################
#Define a function to manage the addition and removal of technicans
def HumanRecources(Num_employee0,Employee_menu0):
   x=0
   print("Would you like to adjust the staffing arrangement?")
   #loop until input correctly
   while x<1:
       Choice= input("A, hire new employees\nB, fire employees.\nC, no change.")
       if (Choice in ['A','B','C'])==False:
           print('Please enter a valid option.')
       elif Choice=='A':
           #when hiring
           x2=0
           while x2<1:
               print('Current number of employees is '+ str(Num_employee0))
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
               print('Current number of employees is '+ str(Num_employee0))
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



def CalculateResources(Num_employee0,resources0):
    #sell each fish in turn
    LabourInDays=Num_employee0*5*9
    
    consumption0={'Fertiliser(litres)': 0 ,'Feed (kg)': 0 , 'Salt (kg)': 0}
    
    InCome = 0
    for i in demands.keys():
        #each technician provides nine weeks of labour per quarter
        #LabourInDays=LabourInDays-fishes[i]['Maintenance Time (in days)']*demands[i]['Demand']
        #within the limits of available labor
        
        #loop until input in proper range
        while True:
            
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
                if LabourInDays < fishes[i]['Maintenance Time (in days)']*quantity:
                    print('Insufficient labour: required ' + str(fishes[i]['Maintenance Time (in days)']*quantity) + ' days, available ' + str(LabourInDays) + ' days. Please choose again.')
                    continue
                #check fertilizer
                if resources0['Fertiliser(litres)']*1000 < fishes[i]['Fertilizers (ml)']*quantity:
                    print("Insufficient fertilizers: required {0} litres, available {1} litres. Please choose again.".format(fishes[i]['Fertilizers (ml)']*quantity/1000, resources0['Fertiliser(litres)']))
                    continue
                #check feed
                if resources0['Feed (kg)'] < fishes[i]['Feed (kg)']*quantity:
                    print("Insufficient feed: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Feed (kg)']*quantity, resources0['Feed (kg)']))
                    continue
                #check salt
                if resources0['Salt (kg)'] < fishes[i]['Salt (kg)']*quantity:
                    print("Insufficient salt: required {0} kg, available {1} kg. Please choose again.".format(fishes[i]['Salt (kg)']*quantity, resources0['Salt (kg)']))
                    continue
                
                #calculate the consumption of recources
                consumption0['Fertiliser(litres)'] = consumption0['Fertiliser(litres)'] + fishes[i]['Fertilizers (ml)']*quantity/1000
                consumption0['Feed (kg)'] = consumption0['Feed (kg)'] + fishes[i]['Feed (kg)']*quantity
                consumption0['Salt (kg)'] = consumption0['Salt (kg)'] + fishes[i]['Salt (kg)']*quantity
            
                #Renew the current resources
                resources0['Fertiliser(litres)'] = resources0['Fertiliser(litres)'] - consumption0['Fertiliser(litres)']
                resources0['Feed (kg)'] = resources0['Feed (kg)'] - consumption0['Feed (kg)']
                resources0['Salt (kg)'] = resources0['Salt (kg)'] - consumption0['Salt (kg)']
                
            
                #summary then break
                print('Fish '+ i + ', demand ' + str(demands[i]['Demand']) + ', sell ' + quantity + ' units.')
                InCome = InCome + quantity*demands[i]['Price']
                break
        
    return resources0, InCome
       
CalculateResources(Num_employee,resources)

###########################################################################
#Define a function to 
###########################################################################
#Define a function to renew cash 
#Test
#Employees_menu0=Employees_menu
#Num_employee0=3
#i=3


def RenewCash(Num_employee0, Employees_menu0, InCome0, Fund, resources):
    #add income from selling fishes
    Fund = Fund + InCome0
    
    #pay the salary
    for i in range(0,int(Num_employee0)):
        print('Paid ' + Employees_menu0[i] + ', weekly rate='+ str(WeeklyRate)+' amount ' + str(WeeklyRate*12))
        Fund = Fund - WeeklyRate*12
    
    #payfor warehouses
    #fertilizer
    WarehouseCost0 = WarehouseCost0 + resources['Fertiliser(litres)'] * warehouses_price['Fertiliser(litres)']
    #feed
    WarehouseCost0 = WarehouseCost0 + resources['Feed (kg)'] * warehouses_price['Feed (g)']*1000
    #salt
    WarehouseCost0 = WarehouseCost0 + resources['Salt (kg)'] * warehouses_price['Salt (g)']*1000
    
    Fund = Fund - WarehouseCost0
    
    
    
    
    
    
    
    
    
    
    
    
    
  