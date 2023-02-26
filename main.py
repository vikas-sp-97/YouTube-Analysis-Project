# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from pandas.tseries.offsets import DateOffset
import pandas as pd
from YouTube_trends_analysis import get_final_keyword_set
import argparse


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # val = '2020-01-01'
    # items = pd.to_datetime(val, format='%Y-%m-%d')
    # temp = items - DateOffset(days=1)
    print("number : " + str(name))


def test_func(i):
    return get_final_keyword_set(i)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # final_dataset_list = []
    # for i in range(0, 10):
    #     keywords = test_func(i)
    #     final_dataset_list.append(keywords)
    # print(final_dataset_list)
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args()

    keywords = test_func(int(args.name))
    # print(keywords)

    # print_hi(args.name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
