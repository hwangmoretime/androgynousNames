import pandas


def load_all_df():
    return pandas.read_csv('./raw_data/all_yob.csv')


def df_iterator():
    for year in range(1880, 2014):
        file_name = 'raw_data/yob' + str(year) + '.csv'
        df = pandas.read_csv(file_name)
        df['year'] = year
        yield df
    return
