import requests

#api_key = "02f525afa3c5929d187885af19e18222"

def get_weather(city, api_key):
    # Base URL for the Current Weather Data API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Parameters for the request: city name, your key, and metric units (Celsius)
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        # Raises an error for bad status codes (like 404 or 401)
        response.raise_for_status() 
        
        data = response.json()
        
        city_name = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"\n--- Weather in {city_name} ---")
        print(f"Condition: {desc.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"\n------------------------------")

    except requests.exceptions.HTTPError:
        print("Error: City not found or API key invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    MY_API_KEY = "02f525afa3c5929d187885af19e18222"
    user_city = input("Enter the city name: ")
    get_weather(user_city, MY_API_KEY)