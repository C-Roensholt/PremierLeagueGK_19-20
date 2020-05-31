# 1. Web scrape data for GK stats from Top 5 Leagues
# To web scrape data from fbref.com for all goalkeeper stats

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv

#getting the data source
url_epl = "https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats"
url_laLiga = "https://fbref.com/en/comps/12/keepersadv/La-Liga-Stats"
url_bundes = "https://fbref.com/en/comps/20/keepersadv/Bundesliga-Stats"
url_serieA = "https://fbref.com/en/comps/11/keepersadv/Serie-A-Stats"
url_ligue1 = "https://fbref.com/en/comps/13/keepersadv/Ligue-1-Stats"


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
    
    #find all rows (which contains stats for each gk)
    rows_player = player_table.findAll("tr")
    #loop through every row
    for row in rows_player:
        #check if there is a key: value pair in dict
        if(row.find("th",{"scope":"row"}) != None):
            
            #loops over those rows to find each of the features we want (data-stat tag)
            for f in features_wanted:
                cell = row.find("td", {"data-stat": f}) #
                
                #remove unecessary text
                a = cell.text.strip().encode() 
                text = a.decode("utf-8")
                
                #save data to dictionary (either append new value to feature list or add new key to dictionary with new value as list
                if f in pre_df_player:
                    pre_df_player[f].append(text)
                else:
                    pre_df_player[f] = [text]
    
    df_player = pd.DataFrame.from_dict(pre_df_player)
    return df_player

#save dataframe for each league
df_epl = scrapeURL(url_epl)
df_laLiga = scrapeURL(url_laLiga)
df_bundes = scrapeURL(url_bundes)
df_serieA = scrapeURL(url_serieA)
df_ligue1 = scrapeURL(url_ligue1)

#set player name as index
df_epl.set_index("player", inplace=True)
df_laLiga.set_index("player", inplace=True)
df_bundes.set_index("player", inplace=True)
df_serieA.set_index("player", inplace=True)
df_ligue1.set_index("player", inplace=True)

# #save csv files
# df_epl.to_csv("epl_gk_stats_MD17.csv")
# df_laLiga.to_csv("laLiga_gk_stats_MD17.csv")
# df_bundes.to_csv("bundes_gk_stats_MD17.csv")
# df_serieA.to_csv("serieA_gk_stats_MD17.csv")
# df_ligue1.to_csv("ligue1_gk_stats_MD17.csv")
