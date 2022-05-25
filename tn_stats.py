import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import urllib
import requests

   
   
basic_url = "https://www.les-sports.info/football-championnat-de-tunisie-clp-1-statistiques-sups1635.html"

def get_tab(ind) :


    req = urllib.request.Request(basic_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    df = pd.read_html(webpage, header=0) # Read HTML tables into a list of DataFrame objects.
    
    #print(len(df))
    #print(df[ind])
    return df[ind]


tab = [] #list of tab


tab_28 = "Classement historique basé sur tous les résultats depuis 2004/2005"
tab_27 = "Matchs nuls par matchs joués"
tab_26 =  "Matchs perdus par matchs joués"
tab_25 = "Défaites"
tab_24 = "Matchs nuls"  
tab_23 = "Matchs gagnés par matchs joués" 
tab_22 = "Victoires"
tab_21 = "Matchs joués par participation"
tab_20 = "Nombre de matchs joués"
tab_19 = "Nombre de participations"
tab_18 = "Liste des podiums par ville depuis"
tab_17 = "Liste des podiums depuis 1921/1922"
tab_16 = "Bilan par équipe depuis 1921/1922"

tab.append(tab_16)
tab.append(tab_17)
tab.append(tab_18)
tab.append(tab_19)
tab.append(tab_20)
tab.append(tab_21)
tab.append(tab_22)
tab.append(tab_23)
tab.append(tab_24)
tab.append(tab_25)
tab.append(tab_26)
tab.append(tab_27)
tab.append(tab_28)


#############                               CREATION OF STREAMLIT APP                  ##########

st.markdown("""
Squad Standard Stats!
*   Pyhon librairies: ** base64, pandas, Streamlit
*   https://fbref.com/en/
""")
st.sidebar.header('User Input Feature')
selected_year = st.sidebar.selectbox('tableau  ', tab)
st.title('  TUNISIA League Stats    ')

i =  tab.index(selected_year) +16

D = get_tab(i)
st.dataframe(D)