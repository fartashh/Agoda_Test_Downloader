from downloader import Downloader
from threading import Thread


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