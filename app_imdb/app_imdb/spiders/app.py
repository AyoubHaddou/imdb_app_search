# Les imports : 
import streamlit as st
import pandas as pd
import numpy as np

# Fonction pour charger les données :
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Import du CSV 
imdb = pd.read_csv("datafram.csv")

#Déclaration de mes variables : 

list_movies = imdb['title'].tolist()

# I convert my Datafram actors colomn to list 
list_actors = []
for i in imdb['actors']:
    for j in i.split(","):
        list_actors.append(j)

# I convert my Datafram country colomn to list 
list_country = []
for i in imdb['Origin country']:
    for j in i.split(','):
        list_country.append(j)

# I convert my Datafram category colomn to list 
list_category = []
for i in imdb["genre"]:
    for j in i.split(','):
        list_category.append(j)

# I convert my Datafram language colomn to list 
list_language = []
for i in imdb["Origin language"]:
    for j in i.split(","):
        list_language.append(j)

# For my slide bar duration between 60min and 400min 
time = [i for i in range (60,400, 30)] 


#Titre de la page
st.title('Make your movie:')
st.sidebar.subheader('Filters :')
st.subheader('Movies explorer:')


# Creation de mes inputs et des filtres :
data_container = st.container()
with data_container :
    checkmovie = st.sidebar.checkbox("Filters")
    if checkmovie :
        duration = st.sidebar.select_slider("By duration", time )
        movie = st.sidebar.multiselect("List of movies", set(list_movies))
        choose_actors = st.sidebar.multiselect('Select your actors',set(list_actors))
        country = st.sidebar.multiselect("Country", set(list_country))
        category = st.sidebar.multiselect('Category',set(list_category))
        language = st.sidebar.multiselect('Language', set(list_language))

        st.write("By Duration" ,imdb[imdb['duration by min'] <= duration])
        st.write( "By movies", imdb[imdb["title"].isin(movie)])
        st.write("By actors" , imdb[imdb['actors'].isin(choose_actors)])
        st.write("By Country" , imdb[imdb['Origin country'].isin(country)])
        st.write("By Category" , imdb[imdb['genre'].isin(category)])
        st.write("By language", imdb[imdb['Origin language'].isin(language)])

all = st.sidebar.checkbox("All")
if all :
    st.write( "Our all Liberary below! ",imdb)



# Mes fonctions de tri dans un containers : 
    # if choose_actor :
    #     st.write(imdb[imdb['actors'].isin(choose_actor)])


    # # Filtre par durée de films : 
    # if duration :
    #     data = st.write(imdb[imdb['duration by min'] <= duration])







#Markdown 
st.markdown(

    " ###### Made by Ayoub "
)
