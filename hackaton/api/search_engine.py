import requests


def find_minzdrav_info(query: str):
    try:
        response = requests.get(f"https://nsi.rosminzdrav.ru/api/data?identifier=1.2.643.5.1.13.13.11.1461&version=6.1475&query={query}&page=1&size=50&queryCount=true", verify=False)
    
        if response.status_code != 200:
            return None
        
        data = response.json()

        return data["list"][0]
    except Exception as ex:
        print(ex)
        return None