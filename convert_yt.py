from pytube import YouTube
from convert_bytes import convert_size
import datetime

class ConvertYt():
    """ class to convert videos"""

    def __init__(self, url):
        """ class constructor """
        self.url = url
        self.yt = YouTube(url)


    def get_title(self):
        """ get videos title """
        return self.yt.title

    def get_tumbnails(self):
        """get tumbnails image from the video"""
        return self.yt.thumbnail_url

    def get_size(self):
        """ get video size """
        list_of_res = []
        for stream in self.yt.streams:
            stream_info = {}
            stream_info['type'] = stream.type
            stream_info['type_deco'] = stream.subtype
            stream_info['res'] = stream.resolution
            stream_info['size'] = convert_size(stream.filesize)
            list_of_res.append(stream_info)
        return list_of_res

    def get_length(self):
        """ get length of the video"""
        conversion = datetime.timedelta(seconds=self.yt.length)
        converted_time = str(conversion)
        return (converted_time)
