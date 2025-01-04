import utils
import charts
#import read_csv
import pandas as pd

def run():
    df = pd.read_csv('./data.csv')
    country = input("Que pais quieres verificar? ")
    continent = input("Que continente quieres revisar? ")
    res = utils.population_by_country2(df, country)
    if len(res) > 0:
        labels, values = utils.getPopulation2(res.iloc[0])
        charts.generate_bar_chart(country, labels, values)
    else:
        print(f'{country} no se encuentra en la base de datos')

    filterContinent = df[df['Continent'] == continent]
    countries, percentages = utils.getWorldPopulationPercentage2(filterContinent.iloc[:])
    charts.generate_pie_chart(continent, countries, percentages)

    '''data = read_csv.read_csv('./app/data.csv') 
    res = utils.population_by_country(data, country)
    if len(res) > 0:
        #country =  res[0]
        labels, values = utils.getPopulation(res[0])
        charts.generate_bar_chart(country, labels, values)
    filtered = list(filter(lambda x: x['Continent'] == continent, data))
    countries, percentages = utils.getWorldPopulationPercentage(filtered)
    charts.generate_pie_chart(continent, countries, percentages)'''

if __name__ == "__main__":
    run()