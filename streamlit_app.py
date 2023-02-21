import streamlit
import pandas as pd

streamlit.title("My parents new healthy dinner 🥗")



streamlit.header("------ Breakfast Menu")

streamlit.text("-> Overnight oats")
streamlit.text("-> Loaded avocado toast")
streamlit.text("-> Yogurt and fruit parfaits")
streamlit.text("-> Broccoli and cheese egg bake")

streamlit.header('------ Favorite Breakfast Menu')

streamlit.text('-> 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('-> 🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('-> 🥑🍞 Hard-Boiled Free-Range Egg')
fruits_list = pd.read_table("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt",sep=",",index_col="Fruit")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

selection = streamlit.multiselect("SELECT SOME FRUITS:", list(fruits_list.index))
fruits_to_show = fruits_list.loc[selection]

streamlit.dataframe(fruits_to_show )




streamlit.header("----------Recieved chq")
chq = pd.read_csv("./cheque.csv",sep=";")
streamlit.dataframe(chq)

 
