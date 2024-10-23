from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan
from Weather import Weather
from Ideal_Params import Ideal_params
from Drone import Drone
import asyncio

class Monitoring:
#	@@ aqui vai mudar que vai entrar o handeling da situação de acordo com o parâmetro ruim
#	@ Função de comparação pré voô
	async def	monitoring_misson_n_drone(drone):
		from Mission import Mission

		previous_status = None

		while 1:
			await Monitoring.refreshing_values(drone)

			current_status = await Monitoring.comparing_values()

			if current_status != previous_status:
				if not current_status:
					print("===========One or more parameters are not great===========")
			# Here is going to be the actions that depending on the the return of the comparing_values
			# will happen. -----(if the params are not good, flyback)------(if they are terrible, land_Now)------
			#if flag == UNTIL_END:

				previous_status = current_status

			if Mission.status == Mission.FINISHED:
				break

#	@@ aqui vai mudar que vai entrar o handeling da situação de acordo com o parâmetro ruim
#	@ Função de comparação pré voô
	async def first_comparation(drone):
		await Monitoring.refreshing_values(drone)
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
		#for param in Ideal_params.DESCRIPTION:
		#	if param == variables.Weather.description:
		#		return True
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

#	@@ aqui vai mudar que vai entrar o handeling da situação de acordo com o parâmetro ruim
#	@ Função de comparação durante o voô
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
		#for param in Ideal_params.DESCRIPTION:
		#	if param == Weather.description:
		#		return True
					#===Battery===#
		if Drone.battery_temp < Ideal_params.BATTERY_TEMP_MIN:
			return False
		if Drone.battery_temp > Ideal_params.BATTERY_TEMP_MAX:
			return False
		if Drone.battery_level < Ideal_params.MIN_BATTERY_IN_FLIGHT:
			return False
					#===drone====#
		#if Drone.distance_to_base > Ideal_params.MAX_BASE_DISTANCE:
		#	return False
		if Drone.absolute_altitude > Ideal_params.MAX_ABSOLUTE_ALTITUDE:
			return False
		if Drone.relative_altitude < Ideal_params.MIN_REALTIVE_ALTITUDE:
			return False
		if Drone.relative_altitude > Ideal_params.MAX_REALTIVE_ALTITUDE:
			return False
		return True

#	@@ so vai mudar se quisermos adicionar mais comparações ao código
#	@ Função que vai atualizar os valores para que a comparação seja feita
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
