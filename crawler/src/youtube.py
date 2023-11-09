import os
import googleapiclient.discovery
from dotenv import load_dotenv
import csv

load_dotenv()

video_ids = [
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

    "d5JRgHy7mMk",
    "CHqEyouf3PQ",
    "ILGcIsxb7F4",
    "8sZSf4bdu2w",
    "ydAmc-oKzgM",
    "lXKSGrgVwuM",
    "HjLqiSADy_s",
    "ulnCcWzl4W4",
    "6RvCOieb1W8",
    "42dZRZkPxBE",
]


def save_comments(youtube, video_id):
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
        pageToken = response['nextPageToken']

        cnt += response['pageInfo']['resultsPerPage']

        comments = []

        items = response['items']
        for item in items:
            comments.append([1, item['snippet']['topLevelComment']
                            ['snippet']['textDisplay']])

        with open(f"data/youtube/TL-{video_id}.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerows(comments)

        if not pageToken or cnt > 1600:
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

    for video_id in video_ids:
        save_comments(youtube, video_id)


if __name__ == "__main__":
    main()
