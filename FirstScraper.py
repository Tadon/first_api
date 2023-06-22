import requests
## variables from first function
data = '' #data setlist from first api function
latitude = 0 #result of api pull first function
longitude = 0 #result of api pull from first function
## variables from second function
location = '' #Location of city in entered zipcode, results from 2nd function
wdata = '' #data setlist from 2nd function


def get_lat_and_lon(zip_code, country_code , api_key):
    
    global data
    global latitude
    global longitude
    complete_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
    response = requests.get(complete_url)
    data= response.json()

    
    if 'name' in data:
        latitude = data['lat']
        longitude = data['lon']
        return data, latitude, longitude
def get_weather(latitude,longitude, api_key):
    global wdata
    global location
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={api_key}"
    response = requests.get(complete_url)
    wdata = response.json()
    temperature = wdata['main']['temp']
    location = wdata['name']
    conditions = wdata['weather'][0]['description']
    print(f"The weather in {location} is {conditions} at {temperature} Farenheit.")
#main function   
country_code = 'US'
api_key = "bb5ee86038e5df334041bc8baaf0c72f"

while True:
    

    zip_code = input("Enter 1 to exit, otherwise enter zipcode here: ")
    
    if zip_code == '1':
        print("Ending program...")
        break
    
    get_lat_and_lon(zip_code, country_code , api_key)
    get_weather(latitude, longitude, api_key)
    
    