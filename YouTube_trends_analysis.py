from pytrends.request import TrendReq
import pandas as pd
from DataReader import get_val
from pandas.tseries.offsets import DateOffset
import pandas as pd


def remove_duplicated(a):
    dup_val = [item for item in a if item.lower() in a]
    dup_val = set([i.lower() for i in dup_val])
    temp_key = [item for item in a if item.lower() not in a]

    return list(dup_val) + temp_key

def get_pytrend_interest(kw_list, trending_date):
    requests_args = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
    }
    pytrends = TrendReq(requests_args=requests_args)
    pytrends.build_payload(kw_list, cat=0, timeframe=trending_date, gprop='')
    return pytrends.interest_over_time()


def get_relavent_keyword(a, trending_date):
    kw_list = a


    gt_o3_ytd1 = get_pytrend_interest(kw_list, trending_date)

    df = pd.DataFrame(gt_o3_ytd1)
    # print(df)
    test_dic = {}
    for row, i in zip(df._iter_column_arrays(), range(0, len(kw_list))):
        if i == len(kw_list):
            continue
        else:
            test_dic[kw_list[i]] = row[0]
    # print(test_dic)

    test_dic = {key: value for key, value in test_dic.items() if value != 0}

    sorted_dic = sorted(test_dic.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_dic)

def get_data_by_trend_day_count(a, trending_dateformat, trending_days):
    trending_dateformat = trending_dateformat + DateOffset(days=1)
    output_list = {}
    for i in range(0, trending_days):
        trending_dateformat = trending_dateformat - DateOffset(days=1)
        trending_date = str(trending_dateformat)[:10] + ' ' + str(trending_dateformat)[:10]
        # trending_date = '2017-11-19 2017-11-19'

        if len(a) > 5:
            temp = a[0:5]
            res = get_relavent_keyword(temp, trending_date)
            final_list = list(res.keys())
            # print(final_list)
            # print("\n---------------")
            for i in range(5, len(a) - 1, 2):
                temp = final_list[0:3] + a[i: i + 2]
                res = get_relavent_keyword(temp, trending_date)
                final_list = list(res.keys())
                # print(final_list)
                # print("\n---------------")
            output_list[trending_date[:10]] = final_list[:3]

        else:
            res = get_relavent_keyword(a, trending_date)
            # dup_val = list(item for item in res.keys() if item.lower() in res.keys())
            # print(dup_val)
            # temp_key = list(item for item in res.keys() if item.lower() not in res.keys())
            # final_list = list(set(temp_key))
            final_list = list(res.keys())
            # print(final_list)
            output_list[trending_date[:10]] = final_list[:3]
            # print("\n---------------")

    print(output_list)
    # print(final_list[:3], "are the most relavent keywords for the tags as of ", trending_date[:10])
    return output_list

def get_data_by_last_trending_data(a, trending_dateformat):
    trending_date = str(trending_dateformat)[:10] + ' ' + str(trending_dateformat)[:10]
    # trending_date = '2017-11-19 2017-11-19'

    if len(a) > 5:
        temp = a[0:5]
        res = get_relavent_keyword(temp, trending_date)
        final_list = list(res.keys())
        # print(final_list)
        # print("\n---------------")
        for i in range(5, len(a) - 1, 2):
            temp = final_list[0:3] + a[i: i + 2]
            res = get_relavent_keyword(temp, trending_date)
            final_list = list(res.keys())
            # print(final_list)
            # print("\n---------------")
    else:
        res = get_relavent_keyword(a, trending_date)
        # dup_val = list(item for item in res.keys() if item.lower() in res.keys())
        # print(dup_val)
        # temp_key = list(item for item in res.keys() if item.lower() not in res.keys())
        # final_list = list(set(temp_key))
        final_list = list(res.keys())
        # print(final_list)
        # output_list[trending_date[:10]] = final_list[:3]
        # print("\n---------------")

    # print(output_list)
    print(final_list[:3], "are the most relavent keywords for the tags as of ", trending_date[:10])
    return final_list[:3]

def get_final_keyword_set(i, GET_BY_TRENDING_DATE_RANGE = False):
    a = get_val(i)[1]
    a = remove_duplicated(a)
    # a = [0,1,2,3,4,5,6,7,8,9,10]
    trending_days = get_val(i)[3]
    val = get_val(i)[0]
    trending_dateformat = pd.to_datetime(val, format='%Y-%m-%d')
    # print(trending_dateformat)
    if GET_BY_TRENDING_DATE_RANGE:
        return get_data_by_trend_day_count(a, trending_dateformat, trending_days)
    else:
        return get_data_by_last_trending_data(a, trending_dateformat)




# print("\n ---------------- \n")
# print(final_dataset_list)
# get_final_keyword_set(3)

