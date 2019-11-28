#!/bin/pyhton3


def normalize(df, col_name, replace=True):
    """Normalize number column in DataFrame

    The normalization is done with max-min equation:
    z = (x - min(x)) / (max(x) - min(x))

    replace -- set to False if it's desired to return new DataFrame
               instead of editing it.
    """
    col = df[col_name]
    norm_col = (col - col.min()) / (col.max() - col.min())

    if replace:
        df[col_name] = norm_col
        return df
    else:
        norm_df = df.copy()
        norm_df[col_name] = norm_col
        return norm_df


def standardize_text(df, col_name, replace=True):
    """Standardize text column in DataFrame

    The standardization is done this way:
    Splittling string into lower caser words and removing trailing 's'

    replace -- set to False if it's desired to return new DataFrame
               instead of editing it.
    """
    standard = []
    for row in df[col_name]:
        entry = []
        for word in row.replace('/', ',').split(','):
            entry.append(word.strip().lower().replace('\'s', ''))
        standard.append(entry)
    # standard = pd.DataFrame(standard, columns=[col_name, 'count'])
    if replace:
        df[col_name] = standard
        return df
    else:
        new_df = df.copy()
        return new_df
