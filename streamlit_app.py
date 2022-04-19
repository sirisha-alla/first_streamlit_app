import streamlit
streamlit.title('My Parents New Healty Dinner')
streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.title('Omega-3 & Blueberry Oatmeal')
streamlit.title('Kale ,Spinach & Rocket Smoothie')
streamlit.title('Hard-Boiled Free-Range Egg')
streamlit.title('My Mom\'s New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.title('🥣 Omega-3 & Blueberry Oatmeal')
streamlit.title('🥗 Kale ,Spinach & Rocket Smoothie')
streamlit.title('🐔 Hard-Boiled Free-Range Egg')
streamlit.title('🥑🍞 Avacado Toast')
streamlit.header('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)                      
# New Section To Display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
