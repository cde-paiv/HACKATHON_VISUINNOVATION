from supabase import create_client, Client
from dotenv import load_dotenv
import os

class Supabase:
	def	__init__(self, link=None, key=None):
		self.link = "https://vxmmktelugsjuwarwdcv.supabase.co"
		self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ4bW1rdGVsdWdzanV3YXJ3ZGN2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk1MzU1ODUsImV4cCI6MjA0NTExMTU4NX0.E0BZD7uOhEZoP0CIWEzrruNy1gucC2uEOBqjj7sZhP8"

	def	Update_table_info(self, table, id, column, new_info):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.update({column: new_info})
				.eq("id", id)
				.execute()
				)

	def	Create_Waypoint_row(self, id, type, name, lat, long, alt):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
			supabase.table("Waypoint")
			.insert({"id": id, "Type": type, "Name": name, "Latitude":lat, "Longitude":long, "Altitude":alt})
			.execute()
			)

	# Mudar aqui a parte do waypoint, pesquisar melhor como fazer
	def	Create_User_row(self, id, username, e_mail, password, first_name, last_name, drone_id, waypoint_id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
			supabase.table("User")
			.insert({"id": id, "Username": username, "e-mail": e_mail, "Password":password, "First_name":first_name, "Last_name":last_name, "Drone_ID":drone_id, "Waypoint":waypoint_id})
			.execute()
			)

	def	Create_Waypoint_row(self, id, type, name, lat, long, alt):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
			supabase.table("Waypoint")
			.insert({"id": id, "Type": type, "Name": name, "Latitude":lat, "Longitude":long, "Altitude":alt})
			.execute()
			)

	def	Create_row(self, table, id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table("table")
				.insert({"id", id})
				.execute()
				)

	def	Delete_row(self, table, id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response =	(
				supabase.table(table).
				delete()
				.eq('id', id)
				.execute()
				)

	def	Read_row(self, table, row_id):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.select("*")
				.eq("id", row_id)
				.execute()
				)

		return response

	def	Read_table(self, table):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)

		response = (
				supabase.table(table)
				.select("*")
				.execute()
				)
		return response

	def	Def_params_mission(self):
		url: str = os.getenv("SUPABASE_URL", self.link)
		key: str = os.getenv("SUPABASE_KEY", self.key)
		supabase: Client = create_client(url, key)
		response = supabase.table("Mission").select("*").eq("id", 1).execute()

		print(response)
		if response.data:
			record = response.data[0]
			# Drone.drone_id = record.get('Drone_id')
			drone_id = record.get('Drone_id')
			Type_of_delivery = record.get('Type_of_delivery')
			Waypoint = record.get('Waypoint')
			Home = record.get('Home')

			print(drone_id)
			print(Type_of_delivery)
			print(Waypoint)
			print(Home)

		response1 = supabase.table("Waypoint").select("*").eq("id", Waypoint).execute()
		response2 = supabase.table("Waypoint").select("*").eq("id", Home).execute()

		if response1.data:
			record = response1.data[0]
			# Waypoint.latitude = record.get('Latitude')
			# Waypoint.longitude = record.get('Longitude')
			# Waypoint.altitude = record.get('Altitude')
			latitude_w = record.get('Latitude')
			longitude_w = record.get('Longitude')
			altitude_w = record.get('Altitude')
		if response2.data:
			record = response1.data[0]
			# mission = Mission()
			# mission.define_home(record.get('Latitude'), record.get('Longitude'), record.get('Altitude'))
			latitude_h = record.get('Latitude')
			longitude_h = record.get('Longitude')
			altitude_h = record.get('Altitude')
		print(f"{latitude_h} {longitude_h} {altitude_h}")
		print(f"{latitude_w} {longitude_w} {altitude_w}")


def	main():
	sup = Supabase()
	print(sup.Read_row("Waypoint", "2"))


main()
