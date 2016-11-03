from downloader import Downloader
from threading import Thread
from Queue import Queue
import argparse


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.downloader = Downloader()

    def run(self):
        while True:
            url = self.queue.get()
            self.downloader.process(url)
            self.queue.task_done()

class DownloadManager(object):
    """
    Initiate it with list of urls and then call .process
    """
    def __init__(self, urls):
        self.urls = urls
        self.queue = Queue()

    def process(self):
        # create workers
        for x in xrange(len(self.urls)):
            worker = DownloadWorker(self.queue)
            worker.daemon = True
            worker.start()

        # Put the tasks into the queue
        for url in self.urls:
            self.queue.put(url)

        self.queue.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--urls', nargs='+', help='<Required> URLS', required=True, dest='urls')
    args = parser.parse_args()
    downloader_manager = DownloadManager(args.urls)
    downloader_manager.process()