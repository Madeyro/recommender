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
        entry = set()
        for word in row.replace('/', ',').split(','):
            entry.add(word.strip().lower().replace('\'s', ''))
        standard.append(entry)

    if replace:
        df[col_name] = standard
        return df
    else:
        new_df = df.copy()
        new_df[col_name] = standard
        return new_df


def dice_coeff(x, y):
    """Computes the Dice coefficient for similarity of two sets"""
    x = set(x.iloc[0])
    y = set(y.iloc[0])

    numer = 2 * len(x & y)
    denom = len(x) + len(y)
    return numer/denom


def jaccard_coeff(x, y):
    """Computes the Jaccard coefficient for similarity of two sets"""
    x = set(x.iloc[0])
    y = set(y.iloc[0])

    numer = len(x & y)
    denom = len(x) + len(y)
    return numer/denom


def custom_coeff(x, y):
    """Computes the custom similarity coefficient of two sets"""
    x = set(x.iloc[0])
    y = set(y.iloc[0])

    numer = len(x & y)*1.5
    denom = len(x) + len(y)
    return numer/denom

