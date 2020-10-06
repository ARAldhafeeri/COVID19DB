import requests
import json
import pandas as pd 
import plotly.graph_objects as go

class Data:
    def __init__(self):
        self.df_deaths= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv') 
        self.df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        self.df_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        self.yesterday_date = self.df_recovered.columns[len(self.df_recovered.columns) - 2]
        self.today_date = self.df_recovered.columns[-1]
    def get_circles_data(self):
        cases = sum(list(self.df_confirmed[self.today_date]))
        deaths = sum(list(self.df_deaths[self.today_date]))
        recovered = sum(list(self.df_recovered[self.today_date]))
        recovered_today = sum(list(self.df_recovered[self.today_date])) - sum(list(self.df_recovered[self.yesterday_date]))
        deaths_today = sum(list(self.df_deaths[self.today_date])) - sum(list(self.df_deaths[self.yesterday_date]))
        confirmed_today = sum(list(self.df_confirmed[self.today_date])) - sum(list(self.df_confirmed[self.yesterday_date]))
        return ({'deaths': deaths, 'cases': cases,'recovered':recovered, 'recovered today': recovered_today,'deaths_today': deaths_today, 'confrimed_today': confirmed_today})
    
    
    def plot_map(self):
        fig = go.Figure()
        fig.add_trace(go.Scattergeo(
        lon = self.df_confirmed['Long'],
        lat = self.df_confirmed['Lat'],
        text = self.df_confirmed[self.today_date],
        marker = dict(
            size = self.df_confirmed[self.today_date]/10000,
            color = "purple",
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
            name ="Confirmed"))
        fig.add_trace(go.Scattergeo(
        lon = self.df_deaths['Long'],
        lat = self.df_deaths['Lat'],
        text = self.df_deaths[self.today_date],
        marker = dict(
            size = self.df_deaths[self.today_date]/10000,
            color = "red",
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
            name ="Deaths"))

        fig.add_trace(go.Scattergeo(
        lon = self.df_recovered['Long'],
        lat = self.df_recovered['Lat'],
        text = self.df_recovered[self.today_date],
        marker = dict(
            size = self.df_recovered[self.today_date]/10000,
            color = "green",
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
            name ="Recovered"))

        fig.add_trace(go.Scattergeo(
        lon = self.df_recovered['Long'],
        lat = self.df_recovered['Lat'],
        text = self.df_recovered["Country/Region"],
        marker = dict(
            size = self.df_recovered[self.today_date]/10000,
            color = "beige",
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
            name ="Country Name"))


        fig.update_layout(
        title_text = 'COVID19 Map visulization<br>(Click on: confirmed, deaths, recovered, country to toggle traces)',
        showlegend = True,
        geo = dict(
            landcolor = 'rgb(217, 217, 217)',
        )
        )


        fig.write_html("templates/map.html")
