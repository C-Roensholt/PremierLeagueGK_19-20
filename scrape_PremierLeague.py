# 1. Web scrape data for Premier League GK stats
# To web scrape data from fbref.com for all goalkeeper stats

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv


#getting the data source
url = "https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats"


def scrapeURL(url):
    res = requests.get(url)
    ## The next two lines get around the issue with comments breaking the parsing.
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')
    #all tables starts with "tbody"
    all_tables = soup.findAll("tbody")
    team_table = all_tables[0]
    player_table = all_tables[1]
    
    #parse player table
    pre_df_player = dict()
    #all the features we want from the table (found in data-stat)
    features_wanted = {"player", "nationality", "squad", "minutes_90s_gk", "goals_against", "pens_allowed", "free_kick_goals_against"
    ,"corner_kick_goals_against", "own_goals_against", "otxg_gk", "otnpxg_per_shot_on_target_against", "otxg_net_gk"
    , "otxg_net_per90_gk", "passes_completed_launched_gk", "passes_launched_gk", "passes_pct_launched_gk", "passes_gk"
    , "passes_throws_gk", "pct_passes_launched_gk", "passes_length_avg_gk", "goal_kicks", "pct_goal_kicks_launched"
    , "goal_kick_length_avg", "crosses_gk", "crosses_stopped_gk", "crosses_stopped_pct_gk", "def_actions_outside_pen_area_gk"
    , "def_actions_outside_pen_area_per90_gk", "avg_distance_def_actions_gk"}
    
    rows_player = player_table.findAll("tr")
    for row in rows_player:
        if(row.find("th",{"scope":"row"}) != None):
            
            for f in features_wanted:
                cell = row.find("td", {"data-stat": f})
                a = cell.text.strip().encode()
                text = a.decode("utf-8")
                if f in pre_df_player:
                    pre_df_player[f].append(text)
                else:
                    pre_df_player[f] = [text]
    
    df_player = pd.DataFrame.from_dict(pre_df_player)
    return df_player

df_epl_GK = scrapeURL(url)

