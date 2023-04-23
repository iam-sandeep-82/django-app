list_rto_office =( 
    ("Select RTO office", "Select RTO office"), 
    ("Mumbai South", "Mumbai South"), 
    ("Navi Mumbai Vashi", "Navi Mumbai Vashi"), 
    ("Mumbai West", "Mumbai West"), 
    ("Mumbai East", "Mumbai East"), 
    ("Kolhapur", "Kolhapur"), 
    ) 

list_fuel_type=( 
    ('Select Fuel Type','Select Fuel Type'),
    ('Petrol','Petrol'),
    ('Petrol+CNG','Petrol + CNG'),
    ('Diesel','Diesel'),
    ('CNG','CNG'),

    ) 

list_fine_charge =( 
    ("select", "select"), 
    ("Driving without license", "Driving without license"), 
    ("Unauthorized use of vehicles", "Unauthorized use of vehicles"), 
    ("Driving without qualification", "Driving without qualification"), 
    ("Rash Driving", "Rash Driving"), 
    ("Speeding", "Speeding"), 
    ("Drunken Driving", "Drunken Driving"), 
    )

dict_challan={
   'stay this empty':'', 'Driving without license':2000 ,'Unauthorized use of vehicles':5000,'Driving without qualification':10000,'Rash Driving':5000 ,'Speeding':1000, 'Drunken Driving':2000
}

# state='Andhra Pradesh, Assam, Arunachal Pradesh, Bihar, Goa, Gujarat, Jammu and Kashmir, Jharkhand, West Bengal, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Orissa'
# states=list(state.split(','))

# new_states=[]
# for st in states:
#     new_states.append((st,st))

list_states=(
   ('select','select'), (' Maharashtra', ' Maharashtra'),('Andhra Pradesh', 'Andhra Pradesh'), (' Assam', ' Assam'), (' Arunachal Pradesh', ' Arunachal Pradesh'), (' Bihar', ' Bihar'), (' Goa', ' Goa'), (' Gujarat', ' Gujarat'), (' Jammu and Kashmir', ' Jammu and Kashmir'), (' Jharkhand', ' Jharkhand'), (' West Bengal', ' West Bengal'), (' Karnataka', ' Karnataka'), 
('Kerala', ' Kerala'), (' Madhya Pradesh', ' Madhya Pradesh'), (' Manipur', ' Manipur'), (' Meghalaya', ' Meghalaya'), (' Mizoram', ' Mizoram'), (' Nagaland', ' Nagaland'), (' Orissa', ' Orissa')
)




list_of_vech_class=(
    ('Select COV', 'Select COV'),   
    ('MCWOG','MCWOG'), 
    ('CVG', 'CVG') ,
    ('MCWOG/FVG','MCWOG/FVG'),  
    ('LMV-NT','LMV-NT'),   
    ('MGV', 'MGV'), 
    ('HMV', 'HMV'),   
    ('HPMV/HTV','HPMV/HTV'),
)

list_status=(
    ('ACTIVE','ACTIVE'),
    ('EXPIRE','EXPIRE'),
)
    