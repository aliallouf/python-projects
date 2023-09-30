import tkinter as tk
import requests

def get_weather(city):
    api_key = ""
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception if the request was not successful
        weather_data = response.json()

        if weather_data.get("cod") == "404":
            result_label.config(text="City not found.", fg="red")
        else:
            weather = weather_data["weather"][0]["main"]
            temperature_fahrenheit = round(weather_data["main"]["temp"])
            temperature_celsius = round((temperature_fahrenheit - 32) * 5/9)
            result_label.config(text=f"The weather in {city} is: {weather}\n"
                                     f"The temperature in {city} is: {temperature_fahrenheit}°F / {temperature_celsius}°C", fg="black")
    except requests.exceptions.RequestException as e:
        result_label.config(text="An error occurred while making the request: " + str(e), fg="red")

def get_weather_button_click():
    city = city_entry.get()
    get_weather(city)

def clear_button_click():
    city_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

# Create a tkinter window
window = tk.Tk()
window.geometry("400x200")  # Set the initial size of the window
window.title("Weather App")

# Create input fields and buttons
city_label = tk.Label(window, text="Enter the city name:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

button_frame = tk.Frame(window)
button_frame.pack()

get_weather_button = tk.Button(button_frame, text="Get Weather", command=get_weather_button_click)
get_weather_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear_button_click)
clear_button.pack(side=tk.LEFT)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the tkinter event loop
window.mainloop()
