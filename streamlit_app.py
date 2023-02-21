import streamlit
import pandas as pd

streamlit.title("My parents new healthy dinner 🥗")



streamlit.header("------ Breakfast Menu")

streamlit.text("-> Overnight oats")
streamlit.text("-> Loaded avocado toast")
streamlit.text("-> Yogurt and fruit parfaits")
streamlit.text("-> Broccoli and cheese egg bake")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.header('------ Favorite Breakfast Menu')

streamlit.text('-> 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('-> 🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('-> 🥑🍞 Hard-Boiled Free-Range Egg')





streamlit.header("----------Recieved chq")
chq = pd.read_csv("./cheque.csv")
streamlit.text(chq)

 
