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
        self.mapbox_token = 'pk.eyJ1IjoiYXJhbGRoYWZlZXJpIiwiYSI6ImNrZzBtMHY5YTJpd3EycXM4aWJuenIzeXUifQ.H3dQr4j_qqb-H2Z8KICinw'
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
    
    def get_cleaned_data(self):
        data = [self.df_deaths['Country/Region'], self.df_confirmed['Lat'], self.df_confirmed['Long'], self.df_confirmed[self.today_date], self.df_recovered[self.today_date], self.df_deaths[self.today_date]]
        headers = ['Country', 'Lat', 'Long','Confirmed', 'Recovered', 'Deaths' ]
        cleaned_data = pd.concat(data, axis=1, keys=headers)
        return cleaned_data