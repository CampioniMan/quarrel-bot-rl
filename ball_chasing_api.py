import requests

replay_date_after = "2020-01-01T00:00:05Z"


def run_http_request(uri, token, payload=None):
	header = {"Authorization": token}
	return requests.get(uri, payload, headers=header)


def ping(token):
	uri = "https://ballchasing.com/api/"
	return run_http_request(uri, token)


def get_replays_from_pro(token, player_name, count=1):
	global replay_date_after
	payload = {"player-name": player_name,
				"pro": "true",
				"min_rank": "supersonic-legend",
				"playlist": "ranked-duels",
				"count": count,
				"replay-date-after": replay_date_after}
	uri = "https://ballchasing.com/api/replays"
	return run_http_request(uri, token, payload)
