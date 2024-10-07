from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
import start_mission
import requests
import variables
import asyncio

async def	monitoring_misson_n_drone(drone, flag):
	while 1:
		await refreshing_values(drone)
		if await comparing_values(flag) == False:
			print("===========One or more parameters are not great===========")
		# Here is going to be the actions that depending on the the return of the comparing_values
		# will happen. -----(if the params are not good, flyback)------(if they are terrible, land_Now)------
		#if flag == UNTIL_END:
		if start_mission.Mission.status == start_mission.FINISHED:
			break

async def first_comparation(drone):
	refreshing_values(drone)
	if variables.Weather.humidity > variables.Ideal_params.HUMIDITY:
		return False
	if variables.Weather.wind > variables.Ideal_params.WIND:
		return False
	if variables.Weather.visibility < variables.Ideal_params.VISIBILITY:
		return False
	if variables.Weather.temp < variables.Ideal_params.MIN_TEMP:
		return False
	if variables.Weather.temp > variables.Ideal_params.MAX_TEMP:
		return False
	#for param in Ideal_params.DESCRIPTION:
	#	if param == variables.Weather.description:
	#		return True
				#===Battery===#
	if variables.Drone.battery_temp < variables.Ideal_params.BATTERY_TEMP_MIN:
		return False
	if variables.Drone.battery_temp > variables.Ideal_params.BATTERY_TEMP_MAX:
		return False
	if variables.Drone.battery_level < variables.Ideal_params.MIN_BATTERY_TAKEOFF:
		return False
				#===drone====#
	if variables.Drone.absolute_altitude > variables.Ideal_params.MAX_ABSOLUTE_ALTITUDE:
		return False
	return True

async def	comparing_values():
				#===weather===#
	if variables.Weather.humidity > variables.Ideal_params.HUMIDITY:
		return False
	if variables.Weather.wind > variables.Ideal_params.WIND:
		return False
	if variables.Weather.visibility < variables.Ideal_params.VISIBILITY:
		return False
	if variables.Weather.temp < variables.Ideal_params.MIN_TEMP:
		return False
	if variables.Weather.temp > variables.Ideal_params.MAX_TEMP:
		return False
	#for param in Ideal_params.DESCRIPTION:
	#	if param == variables.Weather.description:
	#		return True
				#===Battery===#
	if variables.Drone.battery_temp < variables.Ideal_params.BATTERY_TEMP_MIN:
		return False
	if variables.Drone.battery_temp > variables.Ideal_params.BATTERY_TEMP_MAX:
		return False
	if variables.Drone.battery_level < variables.Ideal_params.MIN_BATTERY_IN_FLIGHT:
		return False
				#===drone====#
	#if variables.Drone.distance_to_base > variables.Ideal_params.MAX_BASE_DISTANCE:
	#	return False
	if variables.Drone.absolute_altitude > variables.Ideal_params.MAX_ABSOLUTE_ALTITUDE:
		return False
	if variables.Drone.relative_altitude < variables.Ideal_params.MIN_REALTIVE_ALTITUDE:
		return False
	if variables.Drone.relative_altitude > variables.Ideal_params.MAX_REALTIVE_ALTITUDE:
		return False
	return True

async def	refreshing_values(drone):
	async for battery in drone.telemetry.battery():
		break
	async for position in drone.telemetry.position():
		break
	variables.Drone.latitude = position.latitude_deg
	variables.Drone.longitude = position.longitude_deg
	variables.Drone.absolute_altitude = position.absolute_altitude_m
	variables.Drone.relative_altitude = position.relative_altitude_m
	variables.Drone.battery_level = battery.remaining_percent
	variables.Drone.battery_temp = battery.temperature_deg
	variables.Weather.get_weather(position.latitude_deg, position.longitude_deg)
