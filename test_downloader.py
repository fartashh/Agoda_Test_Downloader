import unittest
from downloader import Downloader
import os
import json


class DownloadManagerTestCase(unittest.TestCase):
    def setUp(self):
        with open('config.json') as config:
            self.config = json.load(config)
        self.downloader = Downloader()

    def test_http_protocol(self):
        url = "http://mirror.aarnet.edu.au/pub/squid/squid/squid-4.0.15.tar.gz"
        file_name = url.split('/')[-1]
        size = 5146779
        self.downloader.process(url)
        file_path = os.path.join(self.config['download_location'], file_name)
        self.assertEqual(os.path.getsize(file_path), size)
