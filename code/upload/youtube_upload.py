"""
Placeholder script for uploading videos to YouTube using google-api-python-client.

Please provide OAuth credentials and API keys separately.
"""

import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials


def upload_video(video_file, title, description, tags=None, privacy_status="public"):
    creds = None
    # TODO: Load credentials from token.json or similar
    if not creds or not creds.valid:
        # Wait for user to supply credentials
        raise NotImplementedError("YouTube API credentials not provided.")
    youtube = build("youtube", "v3", credentials=creds)
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or []
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    response = request.execute()
    return response
