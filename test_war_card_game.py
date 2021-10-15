import unittest

from war_card_game_code_to_unit_test import Card,main

class TestWarCardGame(unittest.TestCase):
    def test_war_card_game(self):
        deck =[Card("Spades","Ten"),Card("Hearts","Nine"),Card("Clubs","Eight"),Card("Hearts","Seven"),Card("Clubs","Six"),Card("Clubs","Five")]
        self.assertEqual(main(deck),1)#return who win, 1-means win player one,2-means win player two

if __name__=='__main__':
    unittest.main()
