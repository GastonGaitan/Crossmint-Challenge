import requests
import json

def check_response_status(row, column, response):
    if response.status_code == 200:
        print(f"[{row}][{column}] -> successful -> status code {response.status_code}")
    else:
        print(f"[{row}][{column}] -> error -> status code {response.status_code}")

def post_data(url, data):
    response = requests.post(url, json=data)
    check_response_status(data['row'], data['column'], response)

def get_array_dimension(url):
    response = requests.get(url)
    if response.status_code == 200:
        response_content = json.loads(response.content)
        return response_content["map"]['content']

CANDIDATE_ID = "448bc992-6497-48cb-afd8-9f20f312c169"
GUIDANCE_ARRAY_URL = f'https://challenge.crossmint.io/api/map/{CANDIDATE_ID}'
POLIANET_API_URL = 'https://challenge.crossmint.io/api/polyanets'

# I accessed to my candidate map to see the JSON matrix dimensions
if __name__ == '__main__':
    # I fint the array dimension.
    content = get_array_dimension(GUIDANCE_ARRAY_URL)
    # For each row in the array:
    print("Posting Polyanets:")
    for x in range(0, len(content)):
            # For each element in the row:
            for y in range(0, len(content[x])):
                data = {
                    'candidateId': CANDIDATE_ID,
                    'row': x,
                    'column': y
                    }
                if x == y and 1 < x < 9:
                    post_data(POLIANET_API_URL, data)
                    if x != 5 and y !=5:
                        data['column'] = len(content[x]) - 1 - y
                        post_data(POLIANET_API_URL, data)
