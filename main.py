from Monitoring import Monitoring
from Waypoint import Waypoint
from Mission import Mission
from mavsdk import System
from pymavlink import mavutil
from Drone import Drone
import asyncio
import csv # testing with a little database
import sys

#	@ test function
def			print_values():
	from Weather import Weather
	print(f"drone at {Drone.latitude} {Drone.longitude} {Drone.absolute_altitude}")
	print(f"drone battery: {Drone.battery_level} {Drone.battery_temp}")
	print('Temperature:',Weather.temp,'°C')
	print('Wind:',Weather.wind)
	print('Pressure: ',Weather.pressure)
	print('Humidity: ',Weather.humidity)
	print('Description:',Weather.description)
	print('Visibility:',Weather.visibility)

#	@ test function
async def	test_distance(drone):
	from Location import Location
	await Monitoring.refreshing_values(drone)
	print(f"Drone: {Drone.latitude}-{Drone.longitude}-{Drone.absolute_altitude}")
	print(f"Waypoint: {Waypoint.latitude}-{Waypoint.longitude}-{Waypoint.altitude}")
	print(f" max distance = {Drone.max_distance_possible(Drone)}")
	print(f" distance to waypoint = {Location.calc_distance(Drone, Waypoint)}")
	print(f"is it possible {Monitoring.possible_distance()}")


#	@@ essa função vai mudar, porque a base de dados será diferente, oque muda o tipo de leitura
#	@ função lê a base de dados e procura os waypoints
def			finding_points_user(name, waypoint):
	with open('database.csv', 'r') as csvfile:
		csv_reader = csv.reader(csvfile)
		for row in csv_reader:
			if (row[0] == name):
				break
		for row in csv_reader:
			if (row[1] == waypoint):
				Waypoint.latitude = float(row[2])
				Waypoint.longitude = float(row[3])
				Waypoint.altitude = float(row[4])
				print("found == |",row[1], "|")
				return True
	print("Waypoint do not exist, or not in the user")
	return False

async def	pymavlink_esc_status():
	master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

	master.wait_heartbeat()
	print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

	master.mav.command_long_send(
		master.target_system,
		master.target_component,
		mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
		0,
		mavutil.mavlink.MAVLINK_MSG_ID_ESC_STATUS, # message ID
		0, 0, 0, 0, 0, 0)

	while True:
		msg = master.recv_match(type='ESC_STATUS', blocking=True)
		if msg:
			for i in range(msg.esc_count):
				print(f"ESC {i}: RPM: {msg.rpm[i]}, Voltage: {msg.voltage[i]/1000.0}V, Current: {msg.current[i]/100.0}A")


#	definitive main
async def main():
	print("-- program started --")
	drone = System()

	Drone.drone_id = 14550
	what_to_do = sys.argv[1]
	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	if sys.argv[1] == "fly":
		name = sys.argv[2]
		waypoint = sys.argv[3]
		if finding_points_user(name, waypoint) == True:
			await Mission.start_mission(drone)
	if sys.argv[1] == "data":
		await Monitoring.refreshing_values(drone)
		print_values()



""" 	# test distance main
async def	main():
	print("-- program started --")
	drone = System()

	Drone.drone_id = 14550
	what_to_do = sys.argv[1]
	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	if sys.argv[1] == "fly":
		name = sys.argv[2]
		waypoint = sys.argv[3]
		if finding_points_user(name, waypoint) == True:
			await test_distance(drone)
	if sys.argv[1] == "data":
		await Monitoring.first_comparation(drone)
		print_values() """

"""		#test telemetry of motors
	async def main():
	print("-- program started --")
	drone = System()

	Drone.drone_id = 14550
	await drone.connect(system_address="udp://:14550")
	print("-- drone connected")
	async for battery in drone.telemetry.battery():
		break
	print(battery.current_battery_a, battery.remaining_percent, battery.temperature_degc)

	await pymavlink_esc_status()

 """


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
