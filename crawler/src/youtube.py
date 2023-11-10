import os
import googleapiclient.discovery
from dotenv import load_dotenv
import csv

load_dotenv()

video_ids_mz = [
    # MZ
    # "AVv2nHuEzu4",
    # "nha4p2e03i4",
    # "2ObTxaHclS8",
    # "UXtPik71hxE",
    # "C16d1Myo8fg",
    # "FoPV2LZtobs",
    # "Dc8xzuog374",
    # "2pi-PKzkwtA",
    # "YQKNhjSG_J0",
    # "MHasUwq3NfU",
    # "uZ5N-YNLIQ0",
    # "M0O2YjP7ngw",
    # "VwPF6ChZYvA",
    # "gFQDBwZ4qrE",
    # "V-ZLuXAuJ30",
    # "WSioacgT3og"
    # "Cba0HVXGDj8",
    # "PtoXze9XGiQ",
    # "t21dFWWkG5c",
    # "xT2gqqFlNQQ",
    "8Hj4z6vKbNU",
    "0dZaeVh8ssE",
    "jkW9WNhUsOs",
    "7x6uYv8iubM",
]

video_ids_tl = [
    # "d5JRgHy7mMk",
    # "CHqEyouf3PQ",
    # "ILGcIsxb7F4",
    # "8sZSf4bdu2w",
    # "ydAmc-oKzgM",
    # "lXKSGrgVwuM",
    # "HjLqiSADy_s",
    # "ulnCcWzl4W4",
    # "6RvCOieb1W8",
    # "42dZRZkPxBE",
    # "jK8UPMSWRRQ",
    # "ib0rbDOBY_k",
    # "gqgXgFc5eHI",
    # "npXaoOA2yS0"
]


def save_comments(youtube, video_id, label):
    pageToken = ''
    cnt = 0

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=pageToken
        )

        response = request.execute()
        try:
            pageToken = response['nextPageToken']
        except:
            pageToken = ''

        cnt += response['pageInfo']['resultsPerPage']

        comments = []

        items = response['items']
        for item in items:
            comments.append([label, item['snippet']['topLevelComment']
                            ['snippet']['textDisplay']])

        with open(f"data/youtube/output.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerows(comments)

        if not pageToken:
            break


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv('API_KEY')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    for video_id in video_ids_mz:
        save_comments(youtube, video_id, 1)

    for video_id in video_ids_tl:
        save_comments(youtube, video_id, 0)


if __name__ == "__main__":
    main()
