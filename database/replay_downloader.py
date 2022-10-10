import requests


def run_http_request(command, headers):
	return requests.get(command, headers=headers)


def ping_ball_chasing_api(token):
	header = {'Authorization': token}
	ping_command = "https://ballchasing.com/api/"
	return run_http_request(ping_command, header)
