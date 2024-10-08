from Monitoring import Monitoring
from Mission import Mission
from mavsdk import System
from Drone import Drone
import asyncio
import sys

# csv -> test como banco de dados

def		print_values():
	from Weather import Weather
	print(f"drone at {Drone.latitude} {Drone.longitude}")
	print(f"drone battery: {Drone.battery_level}")
	print('Temperature:',Weather.temp,'°C')
	print('Wind:',Weather.wind)
	print('Pressure: ',Weather.pressure)
	print('Humidity: ',Weather.humidity)
	print('Description:',Weather.description)
	print('Visibility:',Weather.visibility)


async def main():
	print("-- program started --")
	drone = System()

	Drone.drone_id = 1234
	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	if sys.argv[1] == '1':
		await Mission.start_mission(drone)
	if sys.argv[1] == '2': # test the updating of the values and compare them with the ideal ones
		await Monitoring.first_comparation(drone)
		print_values()

		#print_values()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
