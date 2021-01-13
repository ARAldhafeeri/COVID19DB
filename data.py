import requests
import json
import pandas as pd 
import plotly.express as px
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

    def get_stats_data(self):
        cases_t = sum(list(self.df_confirmed[self.today_date]))
        deaths_t = sum(list(self.df_deaths[self.today_date]))
        recovered_t = sum(list(self.df_recovered[self.today_date]))
        cases_y= sum(list(self.df_confirmed[self.yesterday_date]))
        deaths_y = sum(list(self.df_deaths[self.yesterday_date]))
        recovered_y = sum(list(self.df_recovered[self.yesterday_date]))
        confirmed_today = cases_t - cases_y
        deaths_today = deaths_t - deaths_y
        recovered_today = recovered_t - recovered_y
        confirmed_change = ((cases_t - cases_y) / cases_y) * 100
        recovered_change = ((recovered_t - recovered_y) / recovered_y) * 100
        deaths_change = ((deaths_t - deaths_y) / deaths_y) * 100
        return ({'deaths': "{:,}".format(deaths_t) ,
                'cases': "{:,}".format(cases_t),
                'recovered':"{:,}".format(recovered_t),
                'confirmed_today': "{:,}".format(confirmed_today),
                'deaths_today': "{:,}".format(deaths_today),
                'recovered_today': "{:,}".format(recovered_today),
                'confirmed_change': round(confirmed_change,3),
                'recovered_change': round(recovered_change,3),
                'death_change': round(deaths_change, 3)})
    
    def get_cleaned_data(self):
        data = [self.df_deaths['Country/Region'], self.df_confirmed['Lat'], self.df_confirmed['Long'], self.df_confirmed[self.today_date], self.df_recovered[self.today_date], self.df_deaths[self.today_date]]
        headers = ['Country', 'Lat', 'Long','Confirmed', 'Recovered', 'Deaths' ]
        cleaned_data = pd.concat(data, axis=1, keys=headers)
        return cleaned_data

    def update_maps(self):
        df = self.get_cleaned_data()
        df["Confirmed"] = df['Confirmed'].replace(np.nan, 0)
        df["Deaths"] = df['Deaths'].replace(np.nan, 0)
        df["Recovered"] = df['Recovered'].replace(np.nan, 0)
        fig = px.scatter_geo(df, lat="Lat", lon="Long", color="Country", size="Confirmed",
                  projection="natural earth", hover_name="Country")
        fig.write_html("templates/confirmed_map.html")
        fig2 = px.scatter_geo(df, lat="Lat", lon="Long", color="Country", size="Deaths",
                  projection="natural earth", hover_name="Country")
        fig2.write_html("templates/deaths_map.html")
        fig3 = px.scatter_geo(df, lat="Lat", lon="Long", color="Country", size="Recovered",
                  projection="natural earth", hover_name="Country")
        fig3.write_html("templates/recovered_map.html")

    
    def update_lines(self):
        """ A method to plot all line graphs realtime """
        # Death count line graph
        fig_line_deaths = go.Figure()
        for i in range(0, len(self.time)):
            if i == 257:
                break
            fig_line_deaths.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_deaths.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_deaths.write_html("templates/fig_line_deaths.html")

        # confirmed line graph
        fig_line_confiremed = go.Figure()
        for i in range(0, len(self.time)):
            if i == 257:
                break
            fig_line_confiremed.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_confirmed.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_confiremed.write_html("templates/fig_line_confirmed.html")

        # recovered line graph
        fig_line_recovered = go.Figure()
        for i in range(0, len(self.time)):
            if i == 250:
                break
            fig_line_recovered.add_trace(
                go.Scatter(x=self.time[7:], y =self.df_recovered.iloc[i][4:],
                    name=self.df_deaths.iloc[i][1] ))
        fig_line_recovered.write_html("templates/fig_line_recovered.html")



       

        