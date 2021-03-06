# user stats; the stats are built here from the table 
# note that the stats are being built for player controlled pcs;
# if I implement player creator, users character will be created/stored elsewhere

from data_reader import *
from player_setup import user_name, opponent_name

#combat card dict builder
def user_stats(user_name):
    user_card = {'name': user_name,
                 'score': score_calculator(user_name),
                 'stamina': stamina_calculator(user_name),
                 'speed': speed_calculator(user_name),
                 'offense': offense_calculator(user_name),
                 'defense': defense_calculator(user_name),
                 'special offense': special_offense_calculator(user_name),
                 'special defense': special_defense_calculator(user_name)
                 }
    return user_card

#combat cards; builds a card for the player entering combat and opponent

user_profile = user_stats(user_name)
opponent_profile = user_stats(opponent_name)


