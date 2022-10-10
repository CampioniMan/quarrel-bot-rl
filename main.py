import ball_chasing_api as bc_api
import configparser


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read_file(open(r"config/secret/ballchasing.txt"))
    secret_token = config.get("token section", "token")
    ping_request = bc_api.ping(secret_token)
    match ping_request.status_code:
        case 200:
            print("API available!")
        case 401:
            print("Invalid token while doing ping")
        case 500:
            print("API unavailable while doing ping")
        case _:
            print(f"Unknown error while doing ping ({ping_request.status_code})")

    pro_replay_request = bc_api.get_replays_from_pro(secret_token, "Squishy", 1)
    match ping_request.status_code:
        case 200:
            print("API call worked!")
            print(pro_replay_request.content)
        case 401:
            print("Invalid token")
        case 500:
            print("API unavailable")
        case _:
            print(f"Unknown error ({ping_request.status_code})")
