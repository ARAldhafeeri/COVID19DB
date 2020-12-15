import requests
import json
import pandas as pd 
import plotly.graph_objects as go
import numpy as np

class Data:
    def __init__(self):
        self.df_deaths= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv') 
        self.df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        self.df_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        self.yesterday_date = self.df_recovered.columns[len(self.df_recovered.columns) - 2]
        self.today_date = self.df_recovered.columns[-1]
        self.days = self.df_deaths.columns[4:]
        self.number_of_days = len(self.days)
        self.time = np.arange(0, self.number_of_days+ 6, 1)

    def get_circles_data(self):
        cases = sum(list(self.df_confirmed[self.today_date]))
        deaths = sum(list(self.df_deaths[self.today_date]))
        recovered = sum(list(self.df_recovered[self.today_date]))
        recovered_today = sum(list(self.df_recovered[self.today_date])) - sum(list(self.df_recovered[self.yesterday_date]))
        deaths_today = sum(list(self.df_deaths[self.today_date])) - sum(list(self.df_deaths[self.yesterday_date]))
        confirmed_today = sum(list(self.df_confirmed[self.today_date])) - sum(list(self.df_confirmed[self.yesterday_date]))
        return ({'deaths': deaths, 'cases': cases,'recovered':recovered, 'recovered today': recovered_today,'deaths_today': deaths_today, 'confrimed_today': confirmed_today})
    
    
    def plot_maps(self):
        """ A method to plot all maps with updated data real-time """
        # Confirmed map
        confirmed_map = go.Figure()
        confirmed_map.add_trace(go.Scattergeo(
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

        confirmed_map.write_html("templates/confirmed_map.html")

        # Deaths map
        deaths_map = go.Figure()
        deaths_map.add_trace(go.Scattergeo(
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
        deaths_map.write_html("templates/deaths_map.html")

        # Recovered map
        recovered_map = go.Figure()
        recovered_map.add_trace(go.Scattergeo(
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

        recovered_map.write_html("templates/recovered.html")
       
        # country name map
        country_name_map = go.Figure()
        country_name_map.add_trace(go.Scattergeo(
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
        country_name_map.write_html("templates/country_name_map.html")


    def plot_lines(self):
        """ A method to plot all line graphs realtime """
        # Death count line graph
        fig_line_deaths = go.Figure()
        for i in range(0, len(self.time)):
            if i == 257:
                break
            fig_line_deaths.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_deaths.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_deaths.write_html("templates/line_deaths.html")

        # confirmed line graph
        fig_line_confiremed = go.Figure()
        for i in range(0, len(self.time)):
            if i == 257:
                break
            fig_line_confiremed.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_confirmed.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_confiremed.write_html("templates/fig_line_confiremed.html")
        
        # recovered line graph
        fig_line_recovered = go.Figure()
        for i in range(0, len(self.time)):
            if i == 250:
                break
            fig_line_recovered.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_recovered.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_recovered.write_html("templates/fig_line_recovered.html")
            

    # def plot_bars(self):
    #     """ A method to plot all bar graphs"""
    #     fig_bar_death = go.Figure()
    #     for i in range(0, len(self.time)):
    #         if i == 257:
    #             break
    #         fig_bar_death.add_trace(
    #             go.Bar(x=["Region", "Country"], y =[0,sum(self.df_deaths.iloc[i][4:])],
    #                     name=self.df_deaths.iloc[i][1]))
    #     fig_bar_death.write_html("templates/bar_deaths.html")

    #     fig_bar_confirmed = go.Figure()
    #     for i in range(0, len(self.time)):
    #         if i == 257:
    #             break
    #         fig_bar_confirmed.add_trace(
    #             go.Bar(x=["Region", "Country"], y =[0, sum(self.df_confirmed.iloc[i][4:])],
    #                     name=self.df_confirmed.iloc[i][1]))
    #     fig_bar_confirmed.write_html("templates/fig_bar_confirmed.html")


    #     fig_bar_recovered = go.Figure()
    #     for i in range(0, len(self.time)):
    #         if i == 250:
    #             break
    #         fig_bar_recovered.add_trace(
    #             go.Bar(x=["Region", "Country"], y =[0,sum(self.df_recovered.iloc[i][4:])],
    #                     name=self.df_recovered.iloc[i][1]))
    #     fig_bar_recovered.write_html("templates/fig_bar_recovered.html")


