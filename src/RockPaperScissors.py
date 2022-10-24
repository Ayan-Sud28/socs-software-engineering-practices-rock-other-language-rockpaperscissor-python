import random

from src.ConfigFromFile import ConfigFromFile


class RockPaperScissors:


    config = None
    property = None

    def __init__(self, config=ConfigFromFile()):
        self.config = config
        self.property = config.get_config()

    def display(self, message):
        print(message)

    def get_input(self, message):
        return int(input(message))

    def determine_winner(self, player, computer):
        if player == computer:
            result = "Draw"
        elif (player + 1)%3 == computer:
            result = "Player wins"
        elif (computer + 1)%3 == player:
            result = "Computer Wins"
        return result

    def get_user_choice_request(self, weapons):
        request = "Select "
        for counter in range(len(weapons)):
            request += str(counter) + " for " + weapons[counter] + " "
        return request

    def get_user_choice(self, weapons):
        request = self.get_user_choice_request(weapons)
        player = self.get_input(request)
        if player in [0, 1, 2]:
            self.display("You selected " + weapons[player])
        return player

    def get_computer_choice(self, weapons):
        chosen = random.randint(0,2)
        self.display("Computer chose " + weapons[chosen])
        return chosen

    def set_property(self):
        if self.property == []:
            self.property = self.config.get_config()

    def get_list_of_games(self):
        self.set_property()
        list_of_games = []
        for counter in range(1, len(self.property)):
            list_of_games.append(self.property[counter].split(":")[0])
        return list_of_games

    def get_weapon_lists(self):
        self.set_property()
        weapon_lists = []
        for counter in range(1, len(self.property)):
            weapon_lists.append(self.property[counter].split(":")[1].split(","))
        return weapon_lists

    def get_games_request(self, list_of_games):
        request = "Please select"
        for counter in range(len(list_of_games)):
            request += " " + str(counter) + " - " + list_of_games[counter]
        return request

    def generate_games_list_request(self):
        list_of_games = self.get_list_of_games()
        request = self.get_games_request(list_of_games)
        return request

    def get_game(self):
        request = self.generate_games_list_request()
        user_game = self.get_input(request)
        weapons_lists = self.get_weapon_lists()
        return weapons_lists[user_game]

    def play(self):
        weapon = self.get_game()
        player = self.get_user_choice(weapon)
        while player in [0, 1, 2]:
            computer = self.get_computer_choice(weapon)
            result = self.determine_winner(player, computer)
            self.display(result)
            player = self.get_user_choice(weapon)

def main():
    rock = RockPaperScissors()
    rock.play()

if __name__ == "__main__":
    main()




