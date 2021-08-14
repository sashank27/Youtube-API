from django_cron import CronJobBase, Schedule
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .models import video

class YouTubeApiFetch(CronJobBase):
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.youtube_api_fetch'

    def do(self):
        DEVELOPER_KEY = 'AIzaSyAtuzByPkZeyCX9ZCtAYB0TdmsQqfsFlmY'
        YOUTUBE_API_SERVICE_NAME = 'youtube'
        YOUTUBE_API_VERSION = 'v3'

        try:
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
            request = youtube.search().list(part="snippet", q="cricket", type="video", order="date")
            response = request.execute()

        except HttpError as e:
            print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))

        for item in response['items']:
            Video.objects.create(
                video_id=item['id']['videoId']
                channel_id=item['snippet']['channelId']
                title=item['snippet']['title']
                description=item['snippet']['description']
                channel_title=item['snippet']['channelTitle']
                publish_time=item['snippet']['publishTime']
            )
