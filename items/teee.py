import requests

url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"

try:
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the list of meal categories
        categories = data['meals']
        for category in categories:
            print(category['strCategory'])
    else:
        print("Request failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error:", str(e))
