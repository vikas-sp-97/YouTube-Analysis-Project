import yaml
from yaml.loader import SafeLoader
import os
import json
import googleapiclient.discovery
from DataReader import get_val

# Open the file and load the file
def get_access_key():
    with open('configurationss.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)

    return data['youtube_api']['key']

def get_response(youtube, video_id):
    request = youtube.commentThreads().list(
        part="snippet,id",
        videoId=video_id,
        textFormat='plainText',
        order="relevance"
    )
    response = request.execute()
    return response

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_access_key()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    final_data =[]
    EMPTY_LIST = []
    video_not_found = 0
    for i in range(0, 4547):
        video_id = get_val(i)[2]
        try:
            response = get_response(youtube, video_id)
            res = []
            # formatted_res = json.dumps(response,indent=2)
            # print(type(response))
            count = 0
            for i in response['items']:
                count +=1
                res.append(i['snippet']['topLevelComment']['snippet']['textDisplay'])
                # print(i['snippet']['topLevelComment']['snippet']['textDisplay'])
                # print("\n--------------\n")
            # print(str(count) + " comments fetched for video id: " + video_id)
            final_data.append(res)
            # print(final_data)
        except:
            video_not_found +=1
            final_data.append(EMPTY_LIST)
            print(video_id)
            # print("error!")

    file = open('/Users/vikassp/Desktop/comments.txt', 'w')
    for item in final_data:
        file.write(str(item) + '\n')
    # for i in final_data:
    #     print(i)
    print(str(video_not_found) +" videos not found or are private!")

if __name__ == "__main__":
    main()