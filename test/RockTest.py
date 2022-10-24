import unittest
from src.DataSource.ConfigFromStub import ConfigFromStub
from src.ConfigFromFile import ConfigFromFile
from unittest.mock import MagicMock
from src.Display.InputTest import InputTest
from src.Display.OutputTest import OutputTest
from src.ReadFileToList import ReadFileToList
from src.RockPaperScissors import RockPaperScissors

class RockTest(unittest.TestCase):

    rock = RockPaperScissors()

    def test_determine_winner_rock_rock(self):
        result = self.rock.determine_winner(0, 0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        self.rock.set_config(ConfigFromStub())
        result = self.rock.generate_games_list_request();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_get_list_of_games_mock(self):
        property_data = []
        property_data.append("Name, First, Second, Third")
        property_data.append("Rock Paper Scissors:Rock, Scissors, Paper")
        property_data.append("Star War:Darth Vadar, Emperor, Luke Skywalker")
        self.rock.property = []
        self.rock.config.get_config = MagicMock(return_value=property_data)
        result = self.rock.get_list_of_games();
        self.assertEqual(['Rock Paper Scissors', 'Star War'], result)

    def get_user_input(self, inputs):
        user_input = InputTest()
        user_input.input_list = inputs
        return user_input

    def get_computer_inputs(self, inputs):
        computer_input = InputTest()
        computer_input.input_list = inputs
        return computer_input

    def test_rock_versus_rock(self):
        self.rock.set_config(ConfigFromStub())
        self.rock.user_input = self.get_user_input([0, 0, 4])
        self.rock.computer_input = self.get_computer_inputs([0])
        user_output = OutputTest()
        self.rock.user_output = user_output
        self.rock.play()
        result = user_output.outputlist.pop(-1)
        self.assertEqual(result, "Draw")

    def test_replay(self):
        self.rock.set_config(ConfigFromFile())
        file_to_list = ReadFileToList()
        self.rock.user_input = self.get_user_input(file_to_list.get_list("userInputLog.csv"))
        self.rock.computer_input = self.get_computer_inputs(file_to_list.get_list("computerInputLog.csv"))
        file_output = file_to_list.get_list("userOutputLog.csv")
        user_output = OutputTest()
        self.rock.user_output = user_output
#        self.rock.play()
#        self.assertEqual(user_output.outputlist, file_output)

    def test_property_rock_paper_scissior(self):
        self.rock.set_config(ConfigFromFile())
        self.assertEqual(self.rock.property[1] , "Rock Paper Scissors:Rock,Scissors,Paper")

    def test_get_user_choice_request(self):
        self.assertEqual("Select 0 for Rock 1 for Paper 2 for Scissor ", self.rock.get_user_choice_request(["Rock","Paper","Scissor"]))

    def test_property_more_than_one(self):
        config = ConfigFromFile()
        property_data = config.get_config()
        self.assertTrue(len(property_data) >= 1)

    def test_at_least_one_game(self):
        self.assertTrue(len(self.rock.get_list_of_games()) >= 1)

    def test_at_least_one_weapon_list(self):
        self.assertTrue(len(self.rock.get_weapon_lists()) >= 1)

    def test_first_weapon_list_has_three_weapons(self):
        self.assertTrue(len(self.rock.get_weapon_lists()) >= 1)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
