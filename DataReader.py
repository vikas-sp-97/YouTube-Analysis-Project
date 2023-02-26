import pandas as pd

def get_val(i):
    data = pd.read_csv("/Users/vikassp/Desktop/US_data.csv")
    first_tag = data['tags'][i]
    cat = data['category_id'][i]
    #print(cat)
    tag_items = str(first_tag).split("|")
    # print(tag_items)
    # print(len(tag_items))
    video_id = data['video_id'][i]
    trending_date = data['last_trending_date'][i]
    # print(trending_date)
    trend_day_count = data['trend_day_count'][i]
    return trending_date, tag_items, video_id, trend_day_count

# get_val()