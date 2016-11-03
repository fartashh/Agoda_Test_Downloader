import logging

logging.basicConfig()
import urllib2
import sys
import json
import os


class Downloader(object):
    """
    Downloader responsible to download and validate the downloaded file
    Instantiate it and the call the process with url
    """
    _logger = logging.getLogger('Downloader')

    def __init__(self):
        with open('config.json') as config:
            self.config = json.load(config)

    def process(self, url):
        self.url = url
        self.file_name = self.url.split('/')[-1]
        self.file_path = os.path.join(self.config['download_location'], self.file_name)
        try:
            open_url = urllib2.urlopen(self.url)
            self.meta_data = open_url.info()
            self.file_size = float(self.meta_data.getheaders("Content-Length")[0])
            downloaded_amount = 0.0
            block_size = 8192

            print "\nStart Downloading {} <{}>".format(self.file_name, self.file_size)
            with open(self.file_path, 'wb') as file:
                while True:
                    buffer = open_url.read(block_size)
                    if not buffer:
                        break
                    downloaded_amount += len(buffer)
                    file.write(buffer)
                    self.__update_progress(self.file_name, 100 * downloaded_amount / self.file_size)
            return self
        except urllib2.URLError as ex:
            self._logger.exception('connection refused; invalid URL')
            raise ex
        except Exception as ex:
            self.__validate_downloaded_file()
            self._logger(ex)
            raise ex

    def __update_progress(self, file_name, progress):
        sys.stdout.write('\n%s\n' % file_name)
        sys.stdout.write("[%-50s] %.3f%%" % ('#' * int(progress), progress))
        sys.stdout.flush()
