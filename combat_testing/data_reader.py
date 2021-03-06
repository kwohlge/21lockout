import csv

#sql-like stat ripping function from CSV tables
def player_stat_ripper(table_player_name, table_stat_category):

    rawplayerdata = csv.DictReader(open('../data/players.csv', 'rb'))

    dict_list = []

    for line in rawplayerdata:
        dict_list.append(line)
    
    dict_length = len(dict_list)
    dict_max = dict_length
    dict_counter = 0

    #return dict_lists' index number for a given player's name; see below
    #it's case sensitive; ie 'Lebron James' won't pass but 'LeBron James' does
    player_key = {}

    while dict_counter < dict_max:
        #print dict_counter
        player_key[dict_list[dict_counter].get('Player')] = dict_counter
        dict_counter += 1

    if dict_list[player_key[table_player_name]].get(table_stat_category) is '': 
        return 0 #this may throw errors later if expecting a string like Team or Player
    else:
        return dict_list[player_key[table_player_name]].get(table_stat_category)


#for teams: enter team name and stat field you want; bam you get it
def team_stat_ripper(table_team_name, table_stat_category):

    rawplayerdata = csv.DictReader(open('../data/teams.csv', 'rb'))

    dict_list = []

    for line in rawplayerdata:
        dict_list.append(line)
    
    dict_length = len(dict_list)
    dict_max = dict_length
    dict_counter = 0

    #return dict_lists' index number for a given player's name; see below
    #it's case sensitive; ie Lebron James won't pass but LeBron James does
    team_key = {}

    while dict_counter < dict_max:
        #print dict_counter
        team_key[dict_list[dict_counter].get('team')] = dict_counter
        dict_counter += 1

    return dict_list[team_key[table_team_name]].get(table_stat_category)


#examples
#name = "Jose Barea"
#team = player_stat_ripper(name, 'Team')

#calculates speed; calculated by bref position and team pace
def speed_calculator(name):

    playerteam = player_stat_ripper(name, 'Team')
    team_pace = float(team_stat_ripper(playerteam, 'adj pace'))
    player_base_speed = float(player_stat_ripper(name, 'Position'))

    #i just like the way this made up stat looks, YA'LL
    adj_player_speed = (10 - player_base_speed)*10

    #modifier 1.176 makes Ty lawson fastest player; i took out the modifier
    #there's really no reason for it; it takes away from ability to alter
    player_speed = round(team_pace * adj_player_speed)
    return player_speed


#calculates 'hit points' or rather 'score' needed before they give up
def score_calculator(name):

    player_minutes = float(player_stat_ripper(name, '%Min'))
    #find_max_hp = 
    #couple modifiers here; minimum of 5 hps; 21 is the base score weight; 
    # the 1.266 number should be modified to a generic, like w/speed
    player_hit_points = round(((player_minutes * 1.266)*21) + 5)
    return player_hit_points



def stamina_calculator(name):

    player_minutes = float(player_stat_ripper(name, '%Min'))
    player_age = float(player_stat_ripper(name, 'Age on Jan 1 2012'))

    adj_player_minutes = player_minutes * 1.266 #see above for constant change
    adj_player_age = 100 - player_age

    player_stamina = round(adj_player_minutes * adj_player_age)
    return player_stamina


#still need to fix this one; this is just a test version now
def offense_calculator(name):
    
    player_usage = (float(player_stat_ripper(name, 'USG%'))*.01)
    player_offense = player_usage * float(player_stat_ripper(name, 'ORtg')) * float(player_stat_ripper(name, 'eFG%'))
    adj_player_offense = round((player_offense * 3.5458) + 5)
    return adj_player_offense


#don't know how I'm going to factor these stats into the dice roll checks yet
#that's the main issue, then i can set them better
def special_offense_calculator(name):
    
    player_special_offense = 5 #fix this formula
    return player_special_offense


def defense_calculator(name):
    
    player_defense = 5 #fix this formula
    return player_defense


def special_defense_calculator(name):
    
    player_special_defense = 5 #fix this formula
    return player_special_defense


#build a player_profile class, using all the calculators;
#offense, defense, special offense, special defense, stamina, speed
