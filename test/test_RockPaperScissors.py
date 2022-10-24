import unittest
from src.RockPaperScissors import RockPaperScissors

class RockPaperScissorTest(unittest.TestCase):

    rock = RockPaperScissors()

    def test_determine_winner(self):
        self.assertEqual("Draw", self.rock.determine_winner(0,0))


    def test_get_user_choice_request(self):
        self.assertEqual("Select 0 for Rock 1 for Paper 2 for Scissors ", self.rock.get_user_choice_request(["Rock","Paper","Scissors"]))
if __name__ == "__main__":
    unittest.main()