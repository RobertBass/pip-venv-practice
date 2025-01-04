#import pandas as pd

def getPopulation(country):
    population_dict = {
        '2022': int(country['2022 Population']),
        '2020': int(country['2020 Population']),
        '2015': int(country['2015 Population']),
        '2010': int(country['2010 Population']),
        '2000': int(country['2000 Population']),
        '1990': int(country['1990 Population']),
        '1980': int(country['1980 Population']),
        '1970': int(country['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def getPopulation2(country):
    population_dict2 = {
        '2022': country['2022 Population'],
        '2020': country['2020 Population'],
        '2015': country['2015 Population'],
        '2010': country['2010 Population'],
        '2000': country['2000 Population'],
        '1990': country['1990 Population'],
        '1980': country['1980 Population'],
        '1970': country['1970 Population']
    }
    labels = population_dict2.keys()
    values = population_dict2.values()
    return labels, values 

def getWorldPopulationPercentage(data):
    countries = list(map(lambda item: item['Country/Territory'], data))
    percentages = list(map(lambda item: float(item['World Population Percentage']), data))
    return countries, percentages

def getWorldPopulationPercentage2(df):
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    return countries, percentages


def population_by_country(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))

def population_by_country2(df, country):
    return df[df['Country/Territory'] == country]
    