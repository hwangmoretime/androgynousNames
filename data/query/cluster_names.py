import pandas as pd

from . import load_all_df, df_iterator
import name_clustering


def main():
    for df in df_iterator():
        query(df)
        return


def query(names_df):
    """Takes in a df and reduces counts rows by name. Outputs a df."""
    # df = pd.DataFrame(columns=names_df.columns)
    from pprint import pprint
    pprint(dict(name_clustering.cluster_names(
        names_df[names_df['gender'] == 'F']['name'],
        hash_type=name_clustering.ifuzzy.types.DMetaphone), indent=4))
    # print name_clustering.cluster_names(names_df['name'])


if __name__ == '__main__':
    main()
