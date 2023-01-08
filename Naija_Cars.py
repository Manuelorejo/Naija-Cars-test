import streamlit as st
import pickle


model = pickle.load(open('Naija_Cars_model.pickle','rb'))


st.write("This application helps to estimate the prices of Cars in Nigeria based on features of the desired car. It is built on data from the dataset 'Nigerian_Car_Prices' provided by Kaggle")


make = st.selectbox('Please select your desired make', ['Toyota', 'Lexus', 'Mercedes-Benz', 'Land Rover', 'Acura', 'Ford',
       'Infiniti', 'Peugeot', 'Nissan', 'Hyundai', 'Pontiac', 'Chevrolet',
       'Honda', 'Kia', 'Mazda', 'Mitsubishi', 'Suzuki', 'BMW',
       'Volkswagen', 'Volvo'])

Condition = st.selectbox('Please select the condition you want the car to be in', ['Brand New', 'Foreign Used', 'Nigerian Used'])

fuel = st.selectbox("Please select the type of engine of the desired car", ['Diesel','Electric','Hybrid','Petrol',])

transmission = st.selectbox("Please select the transmission of the car", ['AMT','Automatic','CVT','Manual'])

Mileage = st.number_input('Please input your desired mileage', min_value = 0.0, max_value = 9976050.0)

Year = st.number_input('Please input your desired year of manufacture',min_value = 1996, max_value = 2022)

Engine = st.number_input('Please input your desired engine size', min_value = 1000, max_value= 5700)


Toyota,Lexus,Mercedes_Benz,Land_Rover,Acura,Ford,Infiniti,Peugeot,Nissan,Hyundai,Pontiac,Chevrolet,Honda,Kia,Mazda,Mitsubishi,Suzuki,BMW,Volkswagen,Volvo = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


if make == 'Toyota':
    Toyota = 1
    
elif make == 'Lexus':
    Lexus = 1
    
elif make == 'Mercedes_Benz':
    Mercedes_Benz = 1
    
elif make == 'Land Rover':
    Land_Rover = 1
    
elif make == 'Acura':
    Acura = 1
    
elif make == 'Ford':
    Ford = 1

elif make == 'Infiniti':
    Infiniti = 1
    
elif make == 'Peugeot':
    Peugeot = 1
    
elif make == 'Nissan':
    Nissan = 1
    
elif make == 'Hyundai':
    Hyundai = 1
    
elif make == 'Pontiac':
    Pontiac = 1
    
elif make == 'Chevrolet':
    Chevrolet = 1
    
elif make == 'Honda':
    Honda = 1
    
elif make == 'Kia':
    Kia = 1
    
elif make == 'Mazda':
    Mazda = 1
    
elif make == 'Mitsubishi':
    Mitsubishi = 1
    
elif make == 'Suzuki':
    Suzuki = 1
    
elif make == 'BMW':
    BMW = 1
    
elif make == 'Volkswagen':
    Volkswagen = 1
    
elif make == 'Volvo':
    Volvo = 1
    
    
    
    
Diesel,Electric,Hybrid,Petrol = 0,0,0,0

if fuel == 'Diesel':
    Diesel = 1
    
elif fuel == 'Electric':
    Electric = 1
    
elif fuel == 'Hybrid':
    Hybrid = 1
    
elif fuel == 'Petrol':
    Petrol = 1
    


AMT,Automatic,CVT,Manual = 0,0,0,0

if transmission == 'AMT':
    AMT = 1
    
elif transmission == 'Automatic':
    Automatic = 1
    
elif transmission == 'CVT':
    CVT = 1
    
elif transmission == 'Manual':
    Manual = 1
    


New, Foreign,Nigerian = 0,0,0

if Condition == 'Brand New':
    New = 1
    
elif Condition == 'Foreign Used':
    Foreign = 1
    
elif Condition == 'Nigerian Used':
    Nigerian = 1
    
new_pred = model.predict([[Year,Mileage,Engine,Acura,BMW,Chevrolet,Ford,Honda,Hyundai,Infiniti,Kia,Land_Rover,Lexus,Mazda,Mercedes_Benz,Mitsubishi,Nissan,Peugeot, Pontiac, Suzuki, Toyota,Volkswagen, Volvo,New,Foreign,Nigerian,Diesel,Electric,Hybrid,Petrol,AMT,Automatic,CVT,Manual]])
    
st.write("We predict the price of your car will be {} Naira".format(new_pred))
