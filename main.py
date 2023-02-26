# This is a Main Python script.

import json
from pandas.tseries.offsets import DateOffset
import pandas as pd
from YouTube_trends_analysis import get_final_keyword_set
import argparse

# function to perform main operations fo getting keywords
def test_func(i):
    return get_final_keyword_set(i)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args()

    keywords = test_func(int(args.name))

