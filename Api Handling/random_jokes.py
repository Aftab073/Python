import requests

def fetch_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        jokes = data["data"]
        random_jokes = jokes["data"]
        return random_jokes
    else:
        raise Exception("Failed to fetch the joke")


def main():
    try:
        random_jokes = fetch_jokes()
        for joke in random_jokes:
            print(f"Your joke: {joke['content']}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()


