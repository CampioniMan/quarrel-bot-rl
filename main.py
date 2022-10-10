import database.replay_downloader as rd
import configparser


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read_file(open(r"token.txt"))
    secret_token = config.get("token section", "token")
    status = rd.ping_ball_chasing_api(secret_token)
    match status.status_code:
        case 200:
            print("API available!")
        case 401:
            print("Invalid token")
        case 500:
            print("API unavailable")
        case _:
            print(f"Unknown error ({status.status_code})")


