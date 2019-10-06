#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries #WORKING ONE UNTIL 1997
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Get website URLs from 1970 to 1997, where pro cycling was only cathergorized into one tier.
#The sites are parsed with BeatifulSoup, and the two tables with riders and teams extracted.
#The team's and riders' nationalities and counts are then extracted for each year within a list
website = {i: requests.get('https://firstcycling.com/team.php?y='+str(i)+'&d=1&vis=1').text for i in range(1970,1998)}
soup = {i: BeautifulSoup(website[i],'lxml') for i in range(1970,1998)}
My_table = {i: soup[i].find('table',{'class':'tablesorter'}) for i in range(1970,1998)}
My_table2 = {i: My_table[i].find_next('table',{'class':'tablesorter'}) for i in range(1970,1998)}
team_nat = {i: My_table[i].find_all('td') for i in range(1970,1998)}
cycling_nat = {i: My_table2[i].find_all('td') for i in range(1970,1998)}
Team = {i: {a: team_nat[i][a].text for a in range(0,len(team_nat[i]))} for i in range(1970,1998)}
Nationality = {i: {b: cycling_nat[i][b].text for b in range(0,len(cycling_nat[i]))} for i in range(1970,1998)}

#Lists transformed into dataframes
Team_df = pd.DataFrame(Team)
Nationality_df = pd.DataFrame(Nationality)

#Isolating the unique nationalities within all the years
Team_final_df = pd.DataFrame()
Team_final_df["Country"] = Team_df[1::2].stack().unique()
Nat_final_df = pd.DataFrame()
Nat_final_df["Country"] = Nationality_df[1::2].stack().unique()

#Extraction of the specific numbers for each country, both in nationalities and teams
#Each string is passed through the previous dataframes and, for each year, the information written in a new dataframe
#I know, this could have been writte much easier in couple of rows :D
for j in range(1970,1998):
    Nat_final_df[j] = 0
    for i in range(0,len(Nat_final_df["Country"])):
        if Nationality_df[j].str.contains(Nat_final_df["Country"][i]).any() == True:
            idx = Nationality_df[j].loc[Nationality_df[j] == Nat_final_df["Country"][i]].index
            Nat_final_df[j][i] = Nationality_df[j][idx-1].values
            del idx
        else:
            Nat_final_df[j][i] = 0
            
for j in range(1970,1998):
    Team_final_df[j] = 0
    for i in range(0,len(Team_final_df["Country"])):
        if Team_df[j].str.contains(Team_final_df["Country"][i]).any() == True:
            idx = Team_df[j].loc[Team_df[j] == Team_final_df["Country"][i]].index
            Team_final_df[j][i] = Team_df[j][idx-1].values
            del idx
        else:
            Team_final_df[j][i] = 0

#Same procedure as above, but for the years 1998 to 2019, there are three different pro cycling tiers to explore.
#The sites are parsed with BeatifulSoup, and the two tables with riders and teams extracted.
#The team's and riders' nationalities and counts are then extracted for each year within a list           
website1 = {i: requests.get('https://firstcycling.com/team.php?y='+str(i)+'&d=1&vis=1').text for i in range(1998,2020)}
website2 = {i: requests.get('https://firstcycling.com/team.php?y='+str(i)+'&d=2&vis=1').text for i in range(1998,2020)}
website3 = {i: requests.get('https://firstcycling.com/team.php?y='+str(i)+'&d=3&vis=1').text for i in range(1999,2020)}
soup1 = {i: BeautifulSoup(website1[i],'lxml') for i in range(1998,2020)}
soup2 = {i: BeautifulSoup(website2[i],'lxml') for i in range(1998,2020)}
soup3 = {i: BeautifulSoup(website3[i],'lxml') for i in range(1999,2020)}
My_table1 = {i: soup1[i].find('table',{'class':'tablesorter'}) for i in range(1998,2020)}
My_table1_2 = {i: My_table1[i].find_next('table',{'class':'tablesorter'}) for i in range(1998,2020)}
My_table2 = {i: soup2[i].find('table',{'class':'tablesorter'}) for i in range(1998,2020)}
My_table2_2 = {i: My_table2[i].find_next('table',{'class':'tablesorter'}) for i in range(1998,2020)}
My_table3 = {i: soup3[i].find('table',{'class':'tablesorter'}) for i in range(1999,2020)}
My_table3_2 = {i: My_table3[i].find_next('table',{'class':'tablesorter'}) for i in range(1999,2020)}
team_nat1 = {i: My_table1[i].find_all('td') for i in range(1998,2020)}
cycling_nat1 = {i: My_table1_2[i].find_all('td') for i in range(1998,2020)}
team_nat2 = {i: My_table2[i].find_all('td') for i in range(1998,2020)}
cycling_nat2 = {i: My_table2_2[i].find_all('td') for i in range(1998,2020)}
team_nat3 = {i: My_table3[i].find_all('td') for i in range(1999,2020)}
cycling_nat3 = {i: My_table3_2[i].find_all('td') for i in range(1999,2020)}
Team1 = {i: {a: team_nat1[i][a].text for a in range(0,len(team_nat1[i]))} for i in range(1998,2020)}
Nationality1 = {i: {b: cycling_nat1[i][b].text for b in range(0,len(cycling_nat1[i]))} for i in range(1998,2020)}
Team2 = {i: {a: team_nat2[i][a].text for a in range(0,len(team_nat2[i]))} for i in range(1998,2020)}
Nationality2 = {i: {b: cycling_nat2[i][b].text for b in range(0,len(cycling_nat2[i]))} for i in range(1998,2020)}
Team3 = {i: {a: team_nat3[i][a].text for a in range(0,len(team_nat3[i]))} for i in range(1999,2020)}
Nationality3 = {i: {b: cycling_nat3[i][b].text for b in range(0,len(cycling_nat3[i]))} for i in range(1999,2020)}

#Lists transformed into dataframes
Team_df1 = pd.DataFrame(Team1)
Nationality_df1 = pd.DataFrame(Nationality1)
Team_df2 = pd.DataFrame(Team2)
Nationality_df2 = pd.DataFrame(Nationality2)
Team_df3 = pd.DataFrame(Team3)
Nationality_df3 = pd.DataFrame(Nationality3)
Team_final_df1 = pd.DataFrame()
Team_final_df1["Country"] = Team_df1[1::2].stack().unique()
Nat_final_df1 = pd.DataFrame()
Nat_final_df1["Country"] = Nationality_df1[1::2].stack().unique()
Team_final_df2 = pd.DataFrame()
Team_final_df2["Country"] = Team_df2[1::2].stack().unique()
Nat_final_df2 = pd.DataFrame()
Nat_final_df2["Country"] = Nationality_df2[1::2].stack().unique()
Team_final_df3 = pd.DataFrame()
Team_final_df3["Country"] = Team_df3[1::2].stack().unique()
Nat_final_df3 = pd.DataFrame()
Nat_final_df3["Country"] = Nationality_df3[1::2].stack().unique()


#Extraction of the specific numbers for each country, both in nationalities and teams
#Each string is passed through the previous dataframes and, for each year, the information written in a new dataframe
#Again, could have been probably done so much easier and faster, but it works :D
for j in range(1998,2020):
    Nat_final_df1[j] = 0
    for i in range(0,len(Nat_final_df1["Country"])):
        if Nationality_df1[j].str.contains(Nat_final_df1["Country"][i]).any() == True:
            idx = Nationality_df1[j].loc[Nationality_df1[j] == Nat_final_df1["Country"][i]].index
            Nat_final_df1[j][i] = Nationality_df1[j][idx-1].values
            del idx
        else:
            Nat_final_df1[j][i] = 0

for j in range(1998,2020):
    Nat_final_df2[j] = 0
    for i in range(0,len(Nat_final_df2["Country"])):
        if Nationality_df2[j].str.contains(Nat_final_df2["Country"][i]).any() == True:
            idx = Nationality_df2[j].loc[Nationality_df2[j] == Nat_final_df2["Country"][i]].index
            Nat_final_df2[j][i] = Nationality_df2[j][idx-1].values
            del idx
        else:
            Nat_final_df2[j][i] = 0
            
for j in range(1999,2020):
    Nat_final_df3[j] = 0
    for i in range(0,len(Nat_final_df3["Country"])):
        if Nationality_df3[j].str.contains(Nat_final_df3["Country"][i]).any() == True:
            idx = Nationality_df3[j].loc[Nationality_df3[j] == Nat_final_df3["Country"][i]].index
            Nat_final_df3[j][i] = Nationality_df3[j][idx-1].values
            del idx
        else:
            Nat_final_df3[j][i] = 0
            
for j in range(1998,2020):
    Team_final_df1[j] = 0
    for i in range(0,len(Team_final_df1["Country"])):
        if Team_df1[j].str.contains(Team_final_df1["Country"][i]).any() == True:
            idx = Team_df1[j].loc[Team_df1[j] == Team_final_df1["Country"][i]].index
            Team_final_df1[j][i] = Team_df1[j][idx-1].values
            del idx
        else:
            Team_final_df1[j][i] = 0
            
for j in range(1998,2020):
    Team_final_df2[j] = 0
    for i in range(0,len(Team_final_df2["Country"])):
        if Team_df2[j].str.contains(Team_final_df2["Country"][i]).any() == True:
            idx = Team_df2[j].loc[Team_df2[j] == Team_final_df2["Country"][i]].index
            Team_final_df2[j][i] = Team_df2[j][idx-1].values
            del idx
        else:
            Team_final_df2[j][i] = 0
            
for j in range(1999,2020):
    Team_final_df3[j] = 0
    for i in range(0,len(Team_final_df3["Country"])):
        if Team_df3[j].str.contains(Team_final_df3["Country"][i]).any() == True:
            idx = Team_df3[j].loc[Team_df3[j] == Team_final_df3["Country"][i]].index
            Team_final_df3[j][i] = Team_df3[j][idx-1].values
            del idx
        else:
            Team_final_df3[j][i] = 0

#The dataframes of the 1998-2019 riders nationalities extraction are merged together,
#and then combined with the 1970-1997 dataframes.
#All the null values are filled with zero
df1_team = Team_final_df1.set_index('Country').add(Team_final_df2.set_index('Country'), fill_value=0).reset_index()
df2_team = df1_team.set_index('Country').add(Team_final_df3.set_index('Country'), fill_value=0).reset_index()
Team_final_final = df2_team.set_index('Country').add(Team_final_df.set_index('Country'), fill_value=0).reset_index()
Team_final_final = Team_final_final.fillna(0)

#The dataframes of the 1998-2019 teams nationalities extraction are merged together,
#and then combined with the 1970-1997 dataframes.
#All the null values are filled with zero
df1_nat = Nat_final_df1.set_index('Country').add(Nat_final_df2.set_index('Country'), fill_value=0).reset_index()
df2_nat = df1_nat.set_index('Country').add(Nat_final_df3.set_index('Country'), fill_value=0).reset_index()
Nat_final_final = df2_nat.set_index('Country').add(Nat_final_df.set_index('Country'), fill_value=0).reset_index()
Nat_final_final = Nat_final_final.fillna(0)

#The two final dataframes are exported as excel.
Nat_final_final.to_excel("Nationality_Cycling.xlsx")
Team_final_final.to_excel("Team_Cycling.xlsx")


# In[ ]:




