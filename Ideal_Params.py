#	@ defining costs of Ideal_Params to fly, based on the drone documentation
class Ideal_params:
	#====weather====#
	VISIBILITY = 100
	HUMIDITY = 80 # 80%
	WIND = 10 # m/s
	DESCRIPTION = [
					"Clear",
					"Cloudy",
				  ]
	MIN_TEMP = 278
	MAX_TEMP = 318
	#=====battery=====#
	FULL_LOADED_BATTERY = 1000 # Wats
	DIST_PER_W = 100 # meters
	MIN_BATTERY_TAKEOFF = 80
	MIN_BATTERY_IN_FLIGHT = 30
	BATTERY_TEMP_MIN = 283
	BATTERY_TEMP_MAX = 333
	#======drone======#
	MAX_BASE_DISTANCE = 8000 # 8km
	MAX_ABSOLUTE_ALTITUDE = 4500
	MIN_REALTIVE_ALTITUDE = 10
	MAX_REALTIVE_ALTITUDE = 120
	MAXIMUM_TAKEOFF_MASS = 29.0 # drone + gadgets + shipment
	MAXIMUM_TAKEOFF_OPEN_MASS = 24.9 # drone + gadgets + shipment
