import read_csv
import charts
import utils

def run():
    data = read_csv.read_csv('./world_population.csv')
    country = input('Please input a country name: ')
    match = utils.population_by_country(data, country)
    if len(match) > 0:
        country_dict = match[0]
        labels, values = utils.get_population(country_dict)
        charts.generate_bar_chart(labels, values)
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    # countries = list(map(lambda x: x['Country/Territory'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    countries, percentages = utils.get_percentages(data)
    charts.generate_pie_chart(countries, percentages)
    
if __name__ == '__main__':
    run()