from django_cron import CronJobBase, Schedule
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta, timezone
from django.conf import settings

from .models import Video

class YouTubeApiFetch(CronJobBase):
    RUN_EVERY_MINS = settings.CRON_RUN_FREQENCY_MINS

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.youtube_api_fetch'

    def do(self):
        DEVELOPER_KEYS = settings.API_KEYS
        YOUTUBE_API_SERVICE_NAME = 'youtube'
        YOUTUBE_API_VERSION = 'v3'
        valid_resp = False

        # If the db is empty, fetch all videos published from Jan 1,2021.
        # If not, then fetch all the videos published between the current time and last fetch time interval
        if Video.objects.exists():
            last_request_time = datetime.now() - timedelta(minutes=RUN_EVERY_MINS)
        else:
            last_request_time = datetime(2021,1,1)

        # Iterate over all the keys present in list to execute the query, if successfrom any one of them, break the loop
        for KEY in DEVELOPER_KEYS:
            try:
                youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=KEY)
                request = youtube.search().list(part="snippet", q="official", type="video", order="date",
                                                publishedAfter=last_request_time.replace(microsecond=0, tzinfo=timezone.utc).isoformat('T'))
                response = request.execute()
                valid_resp = True
            except HttpError as e:
                print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))

            if valid_resp:
                break

        if valid_resp:
            for item in response['items']:
                Video.objects.create(
                    video_id=item['id']['videoId'],
                    channel_id=item['snippet']['channelId'],
                    title=item['snippet']['title'],
                    description=item['snippet']['description'],
                    channel_title=item['snippet']['channelTitle'],
                    publish_time=item['snippet']['publishTime']
                )
