from string import Template




#define line header

lineHeader = """
	
	
	
	





------------------------------------------

	
		
			
	"""
	
lineFooter = """
	     
	     Choose from the list above.
------------------------------------------
	"""


lineSpacer = """



------------------------------------------
"""





#define the string body for step 1

step1StringBody = """             STEP ONE
	
	1: Engines
	2: Trucks
	3: Battalion Chiefs
	4: Ambulances
	5: Squads
	"""
	





#define engine list

engineList = """
        ENGINES

        1. E62 
        2. E15
        3. E54
        4. E122
        """




#define truck list
	
truckList = """
	TRUCKS
	
	1. T27
	2. T29
	3. T20
	4. T36
    """






#define battalion chief list
			
battalionChiefList = """
	BATTALION CHIEFS
	
	1. BC18
	2. BC19
	3. BC22
	"""






#define ambulance list

ambulanceList = """
	
	1. A17
	2. A24
	3. A58
	"""
	





#define squad list

squadList = """
	
	1. SQD1
	2. SQD2
	3. SQD5
	"""





# define step 2 header string

stepTwoHeader = """             STEP TWO
	"""





#define the info template

infoTemplate = Template('''
COMPANY:  $company
HOUSE:    $house
ADDRESS:  $address 
TYPE:     $type''')
 

#define eng62 info template 

eng62info = infoTemplate.substitute(company= 'E62', house = 'Engine 62',  address = '34 E 114th ST', type = "Engine")


#define eng54 info template 

eng54info = infoTemplate.substitute(company= 'E54', house = 'Engine 54',  address = '7101 S Parnell AVE', type = "Engine")


#define eng92 info

eng92info = infoTemplate.substitute(company= 'E92', house = 'Engine 92',  address = '3112 W 111th ST', type = "Engine")

#define eng15 info

eng15info = infoTemplate.substitute(company= 'E15', house = 'Engine 15',  address = '8026 S Kedzie AVE', type = "Engine")

#define eng122 info

eng122info = infoTemplate.substitute(company= 'E122', house = 'Engine 122',  address = '101 E 79th ST', type = "Engine")


#define trk27 info

t27info = infoTemplate.substitute(company= 'T27', house = 'Engine 62',  address = '34 E 114th ST', type = "Truck")

#define truck29 info

t29info = infoTemplate.substitute(company= 'T29', house = 'Engine 96',  address = '439 N Waller Ave', type = "Truck")

#define truck20 info template 

t20info = infoTemplate.substitute(company= 'T20', house = 'Engine 54',  address = '7101 S Parnell AVE', type = "Truck")

#define truck36 info

t36info = infoTemplate.substitute(company= 'T36', house = 'Engine 44',  address = '412 N Kedzie', type = "Truck")

#define BC18 info

batt18info = infoTemplate.substitute(company= 'BC18', house = 'Engine 95',  address = '4001 W West End Ave', type = "Battalion Chief")

#define BC19 info

batt19info = infoTemplate.substitute(company= 'BC19', house = 'Engine 54',  address = '7101 S Parnell Ave', type = "Battalion Chief")

#define BC22 info

batt22info = infoTemplate.substitute(company= 'BC22', house = 'Engine 62',  address = '34 E 114th ST', type = "Battalion Chief")

#define ambulance 17 info

amb17info = infoTemplate.substitute(company= 'AMB17', house = 'Engine 92',  address = '3112 W 111th st', type = "Ambulance")

#define ambulance 24 info

amb24info = infoTemplate.substitute(company= 'AMB24', house = 'Engine 122',  address = '101 E 79th ST', type = "Ambulance")

#define BC22 info

amb58info = infoTemplate.substitute(company= 'AMB58', house = 'Engine 101',  address = '2242 W 69th ST', type = "Ambulance")

#define amb14 info template 

amb14info = infoTemplate.substitute(company= 'AMB14', house = 'Engine 54',  address = '7101 S Parnell AVE', type = "Ambulance")

#define squad1 info

squad1info = infoTemplate.substitute(company= 'SQUAD1', house = 'Engine 42',  address = '55 W Illinois ST', type = "Squad")

#define squad2 info

squad2info = infoTemplate.substitute(company= 'SQUAD2', house = 'Engine 91',  address = '2821 N Pulaski RD', type = "Squad")

#define squad5 info template 

squad5info = infoTemplate.substitute(company= 'SQUAD5', house = 'Engine 116',  address = '5955 S Ashland AVE', type = "Squad")



#show the choices

print(lineHeader  + step1StringBody + lineFooter)

stepOneChoice = input()
input
if(stepOneChoice == '1'):
                    print(lineHeader + stepTwoHeader + engineList + lineFooter)
                    engListChoice = input()
                    if(engListChoice == '1'):
                        print(lineHeader + eng62info + lineSpacer)
                    elif(engListChoice == '2'):
                        print(lineHeader + eng15info + lineSpacer)
                    elif(engListChoice == '3'):
                        print(lineHeader + eng54info + lineSpacer)
                    elif(engListChoice == '4'):
                        print(lineHeader + eng122info + lineSpacer)
elif(stepOneChoice == '2'):
                print(lineHeader + stepTwoHeader + truckList + lineFooter)
                truckListChoice = input()
                if(truckListChoice == '1'):
                    print(lineHeader + t27info + lineSpacer)
                elif(truckListChoice == '2'):
                    print(lineHeader + t29info + lineSpacer)
                elif(truckListChoice == '3'):
                    print(lineHeader + t20info + lineSpacer)
                elif(truckListChoice == '4'):
                    print(lineHeader + t36info + lineSpacer)
elif(stepOneChoice == '3'):
            print(stepTwoHeader + battalionChiefList + lineFooter)
            bcListChoice = input()
            if (bcListChoice == '1'):
                    print(lineHeader + batt18info + lineSpacer)
            elif(bcListChoice == '2'):
                    print(lineHeader + batt19info + lineSpacer)
            elif(bcListChoice == '3'):
                    print(lineHeader + batt22info + lineSpacer)
elif(stepOneChoice == '4'):
        print(stepTwoHeader + ambulanceList + lineFooter)
        ambListChoice = input()
        if(ambListChoice == '1'):
            print(lineHeader + amb17info + lineSpacer)
        elif(ambListChoice == '2'):
            print(lineHeader + amb24info + lineSpacer)
        elif(ambListChoice == '3'):
            print(lineHeader + amb58info + lineSpacer)
        elif(ambListChoice == '4'):
            print(lineHeader + amb14info + lineSpacer)
elif(stepOneChoice == '5'):
    print(stepTwoHeader + squadList + lineFooter)
squadListChoice = input()
if(squadListChoice == '1'):
    print(lineHeader + squad1info + lineSpacer)
elif(squadListChoice == '2'):
    print(lineHeader + squad2info + lineSpacer)
elif(squadListChoice == '3'):
    print(lineHeader + squad5info + lineSpacer)
