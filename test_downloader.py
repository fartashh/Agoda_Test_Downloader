import unittest
from downloader import Downloader
import os
import json
import urllib2

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

    def test_ftp_protocol(self):
        url = "ftp://ftp.is.co.za/pub/squid/squid-3.1.23.tar.gz"
        file_name = url.split('/')[-1]
        size = 3489539
        self.downloader.process(url)
        file_path = os.path.join(self.config['download_location'], file_name)
        self.assertEqual(os.path.getsize(file_path) , size)

    def test_url_err(self):
        url = "ftp://mirror.aarnet.edu.au/pub/squid/archive/squid-4.0.15.tar.gz"
        with self.assertRaises(urllib2.URLError):
            self.downloader.process(url)

if __name__ == "__main__":
    unittest.main()