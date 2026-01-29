import asyncio
import os
import re
from typing import Union
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
# Fixed: YukkiMusic path use kiya hai
from YukkiMusic.utils.formatters import time_to_seconds
import aiohttp
from YukkiMusic import LOGGER

try:
    from py_yt import VideosSearch
except ImportError:
    from youtubesearchpython.__future__ import VideosSearch

# External API for faster downloads
API_URL = "https://shrutibots.site"

async def download_song(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    if not video_id or len(video_id) < 3:
        return None
    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3")
    if os.path.exists(file_path):
        return file_path
    try:
        async with aiohttp.ClientSession() as session:
            params = {"url": video_id, "type": "audio"}
            async with session.get(f"{API_URL}/download", params=params, timeout=aiohttp.ClientTimeout(total=7)) as response:
                if response.status != 200:
                    return None
                data = await response.json()
                download_token = data.get("download_token")
                if not download_token:
                    return None
                stream_url = f"{API_URL}/stream/{video_id}?type=audio&token={download_token}"
                async with session.get(stream_url, timeout=aiohttp.ClientTimeout(total=300)) as file_response:
                    if file_response.status in [200, 302]:
                        final_url = file_response.headers.get('Location') if file_response.status == 302 else stream_url
                        async with session.get(final_url) as final_resp:
                            with open(file_path, "wb") as f:
                                async for chunk in final_resp.content.iter_chunked(16384):
                                    f.write(chunk)
                        return file_path if os.path.exists(file_path) else None
    except Exception as e:
        LOGGER(__name__).error(f"Download Error: {e}")
        return None

async def download_video(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    if not video_id or len(video_id) < 3:
        return None
    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")
    try:
        async with aiohttp.ClientSession() as session:
            params = {"url": video_id, "type": "video"}
            async with session.get(f"{API_URL}/download", params=params) as response:
                data = await response.json()
                stream_url = f"{API_URL}/stream/{video_id}?type=video&token={data.get('download_token')}"
                async with session.get(stream_url) as final_resp:
                    with open(file_path, "wb") as f:
                        async for chunk in final_resp.content.iter_chunked(16384):
                            f.write(chunk)
                return file_path
    except:
        return None

async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, errorz = await proc.communicate()
    return out.decode("utf-8")

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        return bool(re.search(self.regex, link))

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["title"]

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["thumbnails"][0]["url"].split("?")[0]

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        try:
            downloaded_file = await download_video(link)
            return (1, downloaded_file) if downloaded_file else (0, "Failed")
        except:
            return 0, "Error"

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid: link = self.base + link
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            track_details = {
                "title": result["title"],
                "link": result["link"],
                "vidid": result["id"],
                "duration_min": result["duration"],
                "thumb": result["thumbnails"][0]["url"].split("?")[0],
            }
        return track_details, result["id"]

    async def download(self, link: str, mystic, video: Union[bool, str] = None, videoid: Union[bool, str] = None, **kwargs) -> str:
        if videoid: link = self.base + link
        try:
            if video:
                file_path = await download_video(link)
            else:
                file_path = await download_song(link)
            return (file_path, True) if file_path else (None, False)
        except:
            return None, False
