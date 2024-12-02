from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
from Weather import Weather
from Ideal_Params import Ideal_params
from Drone import Drone
import asyncio

class Monitoring:
#	@ Function thta monitors the drone through the mission
	async def	monitoring_misson_n_drone(drone):
		from Mission import Mission

		previous_status = None

		while 1:
			await Monitoring.refreshing_values(drone)

			current_status = await Monitoring.comparing_values()

			if current_status != previous_status:
				if not current_status:
					print("===========One or more parameters are not great===========")
				previous_status = current_status

			if Mission.status == Mission.FINISHED:
				break

#	@ Check that the drone's and the waypoint's distance is possible
	def possible_distance():
		from Waypoint import Waypoint
		from Location import Location
		if (Location.calc_distance(Drone, Waypoint) < Drone.max_distance_possible(Drone)):
			return True
		return False

#	@@ Receive the drone entity
#	@ Do all the comparations to the ideal parameters to fly
	async def first_comparation(drone):
		await Monitoring.refreshing_values(drone)
		if Monitoring.possible_distance() == False:
			return False
		if Weather.humidity > Ideal_params.HUMIDITY:
			return False
		if Weather.wind > Ideal_params.WIND:
			return False
		if Weather.visibility < Ideal_params.VISIBILITY:
			return False
		if Weather.temp < Ideal_params.MIN_TEMP:
			return False
		if Weather.temp > Ideal_params.MAX_TEMP:
			return False
					#===Battery===#
		if Drone.battery_temp < Ideal_params.BATTERY_TEMP_MIN:
			return False
		if Drone.battery_temp > Ideal_params.BATTERY_TEMP_MAX:
			return False
		if Drone.battery_level < Ideal_params.MIN_BATTERY_TAKEOFF:
			return False
					#===drone====#
		if Drone.absolute_altitude > Ideal_params.MAX_ABSOLUTE_ALTITUDE:
			return False
		return True

#	@@ Receive the drone entity
#	@ Do all the comparations to the ideal parameters during the flight
	async def	comparing_values():
					#===weather===#
		if Weather.humidity > Ideal_params.HUMIDITY:
			return False
		if Weather.wind > Ideal_params.WIND:
			return False
		if Weather.visibility < Ideal_params.VISIBILITY:
			return False
		if Weather.temp < Ideal_params.MIN_TEMP:
			return False
		if Weather.temp > Ideal_params.MAX_TEMP:
			return False
					#===Battery===#
		if Drone.battery_temp < Ideal_params.BATTERY_TEMP_MIN:
			return False
		if Drone.battery_temp > Ideal_params.BATTERY_TEMP_MAX:
			return False
		if Drone.battery_level < Ideal_params.MIN_BATTERY_IN_FLIGHT:
			return False
					#===drone====#
		if Drone.absolute_altitude > Ideal_params.MAX_ABSOLUTE_ALTITUDE:
			return False
		if Drone.relative_altitude < Ideal_params.MIN_REALTIVE_ALTITUDE:
			return False
		if Drone.relative_altitude > Ideal_params.MAX_REALTIVE_ALTITUDE:
			return False
		return True

#	@@ Receive the drone entity
#	@ Refresh all the compared values in order to use them refreshed
	async def	refreshing_values(drone):
		async for battery in drone.telemetry.battery():
			break
		async for position in drone.telemetry.position():
			break
		Drone.latitude = position.latitude_deg
		Drone.longitude = position.longitude_deg
		Drone.absolute_altitude = position.absolute_altitude_m
		Drone.relative_altitude = position.relative_altitude_m
		Drone.battery_level = battery.remaining_percent
		Drone.battery_temp = battery.temperature_degc
		Weather.get_weather(position.latitude_deg, position.longitude_deg)
