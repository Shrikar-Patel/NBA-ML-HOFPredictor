
from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get("https://www.basketball-reference.com/awards/hof.html")
soup = BeautifulSoup(page.content, 'html.parser')

soup.prettify()

year_id = []
name = []
g = []
category = [] 
pts_per_g= [] #points per game
trb_per_g = [] #total rebounds per game
ast_per_g = [] #assists per game
stl_per_g = [] #steals per game
blk_per_g = []  #blocks per game
fg_pct = [] #field goal percentage
fg3_pct = [] # 3 point percentage
ft_pct = [] #free throw percentage
ws = [] #win shares
ws_per_48 = [] #win shares per 48 minutes

list_hof = soup.findAll('tr')
##print(list_hof)


for a in list_hof:
    year_id_g = a.find('th', attrs = {'class':'right', 'data-stat': 'year_id'})
    category_g = a.find('td', attrs = {'class': 'left', 'data-stat' : 'category'})
    game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'g'})
    pts_per_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'pts_per_g'})
    trb_per_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'trb_per_g'})
    ast_per_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'ast_per_g'})
    stl_per_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'stl_per_g'})
    blk_per_game  = a.find('td', attrs = {'class': 'right', 'data-stat' : 'blk_per_g'})
    fg_pct_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'fg_pct'})
    fg3_pct_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'fg3_pct'})
    ft_pct_game = a.find('td', attrs = {'class': 'right', 'data-stat' : 'ft_pct'})
    ws_g = a.find('td', attrs = {'class': 'right', 'data-stat' : 'ws'})
    ws_per_48_g = a.find('td', attrs = {'class': 'right', 'data-stat' : 'ws_per_48'})

    
    name_full_g = a.find('td', attrs = {'class': 'left', 'data-stat' : 'name_full'})
    if(name_full_g != None):
        
        if "WNBA" in name_full_g.text :
            name_full_g = name_full_g.span.extract()
        else:
            name_full_g.span.extract()

            
    
    

    year_id.append(year_id_g.text)  if year_id_g != None else year_id.append(None)
    name.append(name_full_g.text) if name_full_g != None else name.append(None)
    g.append(game.text) if game != None else g.append(None)
    category.append(category_g.text) if category_g != None else category.append(None)
    pts_per_g.append(pts_per_game.text) if pts_per_game != None else pts_per_g.append(None)
    trb_per_g.append(trb_per_game.text) if trb_per_game != None else trb_per_g.append(None)
    ast_per_g.append(ast_per_game.text) if ast_per_game != None else ast_per_g.append(None)
    stl_per_g.append(stl_per_game.text) if stl_per_game != None else stl_per_g.append(None)
    blk_per_g.append(blk_per_game.text) if blk_per_game != None else blk_per_g.append(None)
    fg_pct.append(fg_pct_game.text) if fg_pct_game != None else fg_pct.append(None)
    fg3_pct.append(fg3_pct_game.text) if fg3_pct_game != None else fg3_pct.append(None)
    ft_pct.append(ft_pct_game.text) if ft_pct_game != None else ft_pct.append(None)
    ws.append(ws_g.text) if ws_g != None else ws.append(None)
    ws_per_48.append(ws_per_48_g.text)if ws_per_48_g != None else ws_per_48.append(None)

print("Did it work")
df = pd.DataFrame({'Year' : year_id, 'Name' : name, 'Games' : g, 'Category' : category, 'PPG' :pts_per_g, 'TRB' : trb_per_g, 
'APG' : ast_per_g, 'SPG': stl_per_g, 'BPG' :blk_per_g, 'FGP' : fg_pct, 'FG3P':fg3_pct, 'FTPCT': ft_pct, 'WS' : ws,  'WS_per_48' : ws_per_48 })
df.to_csv('nba_hof.csv')



    






