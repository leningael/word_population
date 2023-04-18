import pandas as pd
import charts

def run():
    df = pd.read_csv('./world_population.csv')
    df = df[df['Continent'] == 'South America']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values 
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()