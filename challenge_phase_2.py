import requests
import json

class universe_entity():
    def __init__(self) -> None:
        self.candidate_id = "448bc992-6497-48cb-afd8-9f20f312c169"
        self.goal_matrix = self.get_goal_matrix()

    def get_goal_matrix(self) -> list:
        response = requests.get(f'https://challenge.crossmint.io/api/map/{self.candidate_id}/goal')
        if response.status_code == 200:
            response_content = json.loads(response.content)
            if "goal" in response_content:
                return response_content["goal"]
            else:
                raise ValueError("Response content does not have a 'goal' field")
        else:
            raise requests.HTTPError(f"HTTP request failed with status code {response.status_code}")
        
    def post_data(self, url, data, entity) -> None:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"{response.status_code} -> Successfull -> {entity} posted at x = {data['row']} | y = {data['column']}")
        else:
            print(f"{response.status_code} -> ERROR -> {entity} NOT posted at x = {data['row']} | y = {data['column']}")

class polyanets(universe_entity):
    def __init__(self) -> None:
        super().__init__()
        self.polyanet_api_url = 'https://challenge.crossmint.io/api/polyanets'
        self.polyanet_data = {
            'candidateId': self.candidate_id,
            'row': 13,
            'column': 13
            }
    
    def center_data(self) -> None:
        self.polyanet_data['row'] = 13
        self.polyanet_data['column'] = 13
    
    def draw_down_right_leaf(self) -> None:

        print("Drawing down right leaf")

        self.center_data()

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']+=1
                self.polyanet_data['column']+=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']+=1
                self.polyanet_data['row']+=1

        self.polyanet_data['row']-=1
        self.polyanet_data['column']-=1

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']-=1
                self.polyanet_data['column']-=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']-=1
                self.polyanet_data['row']-=1

    def draw_top_left_leaf(self) -> None:

        print("Drawing top left leaf")

        self.center_data()

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']-=1
                self.polyanet_data['column']-=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']-=1
                self.polyanet_data['row']-=1

        self.polyanet_data['row']+=1
        self.polyanet_data['column']+=1

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']+=1
                self.polyanet_data['column']+=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']+=1
                self.polyanet_data['row']+=1

    def draw_top_right_leaf(self) -> None:

        print("Drawing top right leaf")

        self.center_data()

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']-=1
                self.polyanet_data['column']+=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']+=1
                self.polyanet_data['row']-=1

        self.polyanet_data['row']+=1
        self.polyanet_data['column']-=1        

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']+=1
                self.polyanet_data['column']-=1
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']-=1
                self.polyanet_data['row']+=1

    def draw_down_left_leaf(self) -> None:

        print("Drawing down left leaf")

        self.center_data()

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']+=1
                self.polyanet_data['column']-=1
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']-=1
                self.polyanet_data['row']+=1

        self.polyanet_data['row']-=1
        self.polyanet_data['column']+=1

        for i in range(8):
            if i < 4:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['row']-=1
                self.polyanet_data['column']+=1
                
            else:
                for j in range(2):
                    super().post_data(self.polyanet_api_url, self.polyanet_data, "Polyanet")
                    self.polyanet_data['column']+=1
                self.polyanet_data['row']-=1

    def draw_flower(self) -> None:
        self.draw_down_right_leaf()
        self.draw_top_left_leaf()
        self.draw_top_right_leaf()
        self.draw_down_left_leaf()

class soloons(universe_entity):
    def __init__(self) -> None:
        super().__init__()
        self.soloon_api_url = 'https://challenge.crossmint.io/api/soloons'
        self.soloon_data = {
            'candidateId': self.candidate_id,
            'row': 0,
            'column': 0,
            'color': None
            }
        self.white_soloons_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'WHITE_SOLOON' == element]
        self.blue_soloons_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'BLUE_SOLOON' == element]
        self.red_soloons_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'RED_SOLOON' == element]
        self.purple_soloons_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'PURPLE_SOLOON' == element]
        self.all_solons_coordinates = {
            "white": self.white_soloons_coordinates,
            "blue": self.blue_soloons_coordinates,
            "red": self.red_soloons_coordinates,
            "purple": self.purple_soloons_coordinates
            }
    
    def post_soloons(self):
        for color, coordinates in self.all_solons_coordinates.items():
            self.soloon_data['color'] = color
            print(f"Posting {self.soloon_data['color']} soloons:")
            for coordinate in coordinates:
                self.soloon_data['row'] = coordinate[0]
                self.soloon_data['column'] = coordinate[1]
                super().post_data(self.soloon_api_url, self.soloon_data, f'{color} Soloon')        

class comeths(universe_entity):
    def __init__(self) -> None:
        super().__init__()
        self.cometh_api_url = 'https://challenge.crossmint.io/api/comeths'
        self.cometh_data = {
            'candidateId': self.candidate_id,
            'row': 0,
            'column': 0,
            'direction': None
            }
        self.up_comeths_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'UP_COMETH' == element]
        self.right_comeths_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'RIGHT_COMETH' == element]
        self.down_comeths_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'DOWN_COMETH' == element]
        self.left_comeths_coordinates = [(i, j) for i, row in enumerate(self.goal_matrix) for j, element in enumerate(row) if 'LEFT_COMETH' == element]
        self.all_comeths_coordinates = {
            "up": self.up_comeths_coordinates,
            "right": self.right_comeths_coordinates,
            "down": self.down_comeths_coordinates,
            "left": self.left_comeths_coordinates
            }
    
    def post_comeths(self):
        for direction, coordinates in self.all_comeths_coordinates.items():
            self.cometh_data['direction'] = direction
            print(f"Posting {self.cometh_data['direction']} Comeths:")
            for coordinate in coordinates:
                self.cometh_data['row'] = coordinate[0]
                self.cometh_data['column'] = coordinate[1]
                super().post_data(self.cometh_api_url, self.cometh_data, f'{direction} cometh')     

# I have been able to find the pattern for the flower drawing.
polyanet = polyanets()
polyanet.draw_flower()

# But I could not find the pattern for soloons and comeths. I would assume they were placed randomly. Nevertheless, I used the data extracted from the goal map provided to post those entities on my megaverse.

soloon = soloons()
soloon.post_soloons()

cometh = comeths()
cometh.post_comeths()
