import requests

class Weather:
	def __init__(self, pressure, humidity, wind, description, temp, visibility):
		Weather.humidity = humidity
		Weather.pressure = pressure
		Weather.wind = wind
		Weather.description = description
		Weather.temp = temp
		Weather.visibility = visibility

#	@@ Receive the position
#	@ Use the weather API to check the weather condition in that place
	def	get_weather(latitude_deg, longitude_deg):
		company_key = "039abd108da2d28ed7c29abf82966f2f"
		src = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude_deg}&lon={longitude_deg}&appid={company_key}"

		return_req = requests.get(src)
		data = return_req.json()
		Weather.humidity = data['main']['humidity']
		Weather.pressure = data['main']['pressure']
		Weather.wind = data['wind']['speed']
		Weather.description = data['weather'][0]['description']
		Weather.temp = data['main']['temp']
		Weather.visibility  = data['visibility']
