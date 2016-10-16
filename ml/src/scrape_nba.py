import requests
import json 

with open('players.json', encoding='utf-8') as data_file:
    players = json.loads(data_file.read())

player_id = str(977)

shot_chart_url = "http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=977&PlusMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&showZones=0"
                
r = requests.get(shot_chart_url)
headers = r.json()['resultSets'][0]['headers']
shots = r.json()['resultSets'][0]['rowSet']