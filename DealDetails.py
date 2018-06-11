import pandas as pd
import requests

class Deals:
	'''
		Class to GET PYR-GTQ Data from Pipedrive using Pipedrive API (https://developers.pipedrive.com/docs/api/v1/#)
	'''

	def __init__(self, api_token, limit = 100, start = 0, num_of_pages = 1):
		'''
		Parameters:
			api_token (str): Pipedrive API Token to Fetch PYR + GTQ Deails

			limit (number): Items shown per page. 
					Default limit is 100, 
					Maximum limit is 500.

			start (number): Pagination Start
					Default start is 0

			num_of_pages(number): Number of Pages to Fetch
					      Default 1
		'''

		assert api_token != "", ("API Token cannot be empty")

		assert isinstance(limit, int), ("limit must be a integer")
		assert isinstance(start, int), ("start must be a integer")
		assert isinstance(num_of_pages, int), ("num_of_pages must be a integer")

		self.api_token = api_token
		self.limit = limit
		self.start = start
		self.num_of_pages = num_of_pages

		# Setup the Flag.
		self.flag = True

	def __pagination_details__(self, additional_details):
		'''
			Helper Function:
				GET the Pagination Information i.e 
					whether more items are availabel in the drive,
					next_start value

				Also, sets flag as True or False
					True: Continue Fetching more Deals
					False: No more Deals to Fetch. STOP

			Parameters:
				additional_details (JSON Formatted Data): Additional Information about Pagination
		'''

		pagination_data = additional_details["pagination"]

		if (pagination_data["more_items_in_collection"]):
			self.flag = True
			self.start = pagination_data["next_start"]

		else:
			self.flag = False

	def __UserPersonDetails__(self, idx, user_data, person_data):
		'''
			Helper Function:
				Parse the User Information and Person Information i.e Deal Owner and Deal User respectively.
				Function takes two value as parameter both of which are JSON Formatted.

			Parameters:
				user_data (JSON Formatted): User Information (Deal Owner ID, Deal Owner Name & Deal Owner Email)
				person_data (JSON Formatted): Person Information (Deal User Name, Deal User Email (or Phone Number), Deal User Value)

			Return:
				A Tuple of User and Person Information
		'''

		# Deal Owner Information
		user_id = user_data["id"]
		user_name = user_data["name"]
		user_email = user_data["email"]

		# Deal User Information
		person_name = person_data["name"]
		person_email = person_data["email"][0]["value"]
		person_id = person_data["value"]

		# Table 1: User and Person Information
		user_person = (idx, user_id, user_name, user_email, person_id, person_name, person_email)

		# Return the tuple of Deal Owner and User Information.
		return user_person

	def __DealDetails__(self, deal_data):
		'''
			Helper Function:
				Parse the Details for a Particular Deal.

			Parameter:
				deal_data (JSON Formatted): Contains all the Details regrading a particular DEAL

			Return:
				A Tuple of Detailed Information for the Deal.
		'''

		# Variables to store the information regrading Deal
		idx = ""
		title = ""
		status = ""
		lost = ""
		category = ""
		event = ""
		gathering = ""
		date = ""
		location = ""
		budget = 0
		artists_requested = ""
		artists_pitched = ""

		try:
			## ID of the Deal
			if deal_data["id"]:
				idx = deal_data["id"]

			## Title of the Deal
			if deal_data["title"]:
				title = deal_data["title"]

			## Status of the Deal
			if deal_data["status"]:
				status = deal_data["status"]

			## lost reason
			if status == "lost":
				lost = deal_data["lost_reason"]

			## Category
			if deal_data["61a501536a4065f5a970be5c6de536cf7ad14078"]:
				category = deal_data["61a501536a4065f5a970be5c6de536cf7ad14078"]

			## Event
			if deal_data["755ded0be98b3ee5157cf117566f0443bd93cc63"]:
				event = deal_data["755ded0be98b3ee5157cf117566f0443bd93cc63"]

			## Gathering Size
			if deal_data["1f9805fdb8715d773f1fc9457545b49c5b05d058"]:
				gathering = deal_data["1f9805fdb8715d773f1fc9457545b49c5b05d058"]

			## Date of the Event
			if deal_data["19c2c12d8fea52c4709cd4ce256b7852bc2b0259"]:
				date = deal_data["19c2c12d8fea52c4709cd4ce256b7852bc2b0259"]

			## Location
			if deal_data["361085abd375a7eb3964f068295f12fe17d9f280_formatted_address"]:
				location = deal_data["361085abd375a7eb3964f068295f12fe17d9f280_formatted_address"]

			## Budget
			if deal_data["value"]:
				budget = deal_data["value"]

			## URL of artists pitched
			if deal_data["00ad4eb98f63fbc58824c74cb67ffafefa51b41b"]:
				artists_pitched = deal_data["00ad4eb98f63fbc58824c74cb67ffafefa51b41b"]

				artists_pitched = artists_pitched.split("\n")

				for i in range(len(artists_pitched)):
					artists_pitched[i] = artists_pitched[i].split("/")[-1]

			## Artists Requested
			if deal_data["ef1b3ca0c720a4c39ddf75adbc38ab4f8248597b"]:
				artists_requested = deal_data["ef1b3ca0c720a4c39ddf75adbc38ab4f8248597b"]

		except Exception as e:
			print (f"[!] Error inside __DealDetails__() function. Exception: {e}")

		finally:
			# Table 2: GTQ Details
			info = (idx, title, category, event, location, budget, gathering, date, artists_pitched, artists_requested, status, lost)

		# Return the Tuple of Deal Details
		return info

	def fetch(self):
		'''
			Function:
				- Sets up the API Endpoint for fetching deals information from Pipedrive API.
				- Fetches Pages of Detail using requests.get() function.

				- Call __UserPersonDetails__() function to parse User-Person Information.
				- Call __DealDetails__() function to parse Deal Details Information.
				- Call __pagination_details__() function to get the value of starting point of next page.

				- Builds Two DataFrame using pd.DataFrame() function for
					- Table 1: User-Person Information
					- Table 2: PYR-GTQ Information

			Additional Info:
				PYR stands for Post Your Requirement.
				GTQ stands for Get the Quotes.
		'''

		## List of User-Person Information
		self.UP_List = list()

		## List of Deal Details
		self.Deal_List = list()

		##
		deal_details = []

		# for each page in num_of_pages
		for _ in range(self.num_of_pages):

			# Continue if more items are availabe to fetch
			if self.flag:

				# Pipedrive API endpoint to Fetch Deal Details
				URL = f"https://api.pipedrive.com/v1/deals?filter_id=61&status=all_not_deleted&start={self.start}&limit={self.limit}&api_token={self.api_token}"

				try:
					# send the request to the pipedrive api endpoint
					r = requests.get(URL)

					# Check whether request was successfull or not
					if r.status_code != 200:
						print (f"[!] Requests Failed with the HTTP Status Code {r.status_code}")
						break

					else:
						# Response of the request that we made is in JSON format
						## get the response using the .json() method
						all_deals = r.json()

						# Check whether the response was success or a failure.
						if (all_deals["success"]):

							# Deal Data
							deal_details = all_deals["data"]

							# for each deal in the data
							for i in range(len(deal_details)):
								try:
									# Call __UserPersonDetails__() function to parse the User-Person Table
									self.UP_List.append(
										self.__UserPersonDetails__(
											deal_details[i]["id"], deal_details[i]["user_id"], deal_details[i]["person_id"]
											)
										)

									# Call __DealDetails__() function to parse Deal Details
									self.Deal_List.append(
										self.__DealDetails__(
											deal_details[i]
											)
										)

								except Exception as e:
									print (f"\n[!!] Error. Exception: {e}\n")
									continue

							# Pagination Information
							self.__pagination_details__(all_deals["additional_data"])

						else:
							print (f"[!] Fetch Failed.")

				except Exception as e:
					print (f"\n[!!] Error Exception: {e}\n")

			else:
				print ("\n\n[X] No More Item to Fetch...")
				break

		# Build DataFrame.

		# User-Person DataFrame
		self.up_df = pd.DataFrame(self.UP_List, columns = ["ID", 
			"Owner_ID", "Owner_Name", "Owner_Email", 
			"User_ID", "User_Name", "User_Email",])

		# GTQ-PYR Details
		self.deal_df = pd.DataFrame(self.Deal_List, columns = ["ID", "Title", 
			"Cateogry", "Event", "Location", "Budget", "Gathering", "Date",
			"Artists_Pitched", "Artists_Requested",
			"status", "lost_reason"])

	def save(self):
		'''
			Function:
				Save the DataFrame as "CSV" in "Data" directory.
		'''
		self.up_df.to_csv("Data/user-person-information.csv", index = False)
		self.deal_df.to_csv('Data/deal-details-infomation.csv', index = False)
