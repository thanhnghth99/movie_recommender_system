import json
import requests
import time
from api_tmdb import API_KEY

base_url = "https://api.themoviedb.org/3/movie/"


def request_movie(input, output):
	json_file = open(output, 'w', encoding="utf-8")

	data = []

	with open(input, 'r') as f:
		for count, line in enumerate(f):
			if count > 0:
				line = line.split(',')
				tmdbId = line[2]
				if len(tmdbId) == 0:
					print("Movie doesn't exist in TMDB database.")
					continue
				url = base_url + tmdbId + "?api_key=" + API_KEY()

				print("Requesting Movie Number: " + str(count))
				res = requests.get(url)

				if res.status_code == 404:
					print("404-Not Found. Movie doesn't exist in TMDB database.")
					continue
				elif res.status_code == 429:
					print("Time out. Waiting for 10 seconds")
					time.sleep(10)
					res = requests.get(url)
				else:
					res.raise_for_status()

				json_file.write(res.text + "\n")
				data.append(json.loads(res.text.strip()))


	json_file.close()

