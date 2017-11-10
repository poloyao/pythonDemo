from watchdog.observers import Observer
from watchdog.events import *
import time
import os

class  FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # def on_moved(self, event):
    #     if event.is_directory:
    #         print("文件夹从 {0} 移动到 {1}".format(event.src_path,event.dest_path))
    #     else:
    #         print("文件从 {0} 移动到 {1}".format(event.src_path,event.dest_path))

    # def on_created(self, event):
    #     if event.is_directory:
    #         print("创建新文件夹:{0}".format(event.src_path))
    #     else:
    #         print("创建新文件:{0}".format(event.src_path))

    # def on_deleted(self, event):
    #     if event.is_directory:
    #         print("删除文件夹:{0}".format(event.src_path))
    #     else:
    #         print("删除文件:{0}".format(event.src_path))

    def on_modified(self, event):
        # if event.is_directory:
        #     print("文件加修改:{0}".format(event.src_path))
        # else:
        #     print("文件修改:{0}".format(event.src_path))
        if not event.is_directory:
            print("文件修改:{0}".format(event.src_path))
            currentPath = event.src_path
            filesize = os.path.getsize(currentPath)
            print(filesize)
            # f = open(currentPath,'r')
            # lines = len(f.readlines())
            # print(lines)

filesize = 0
if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,"d:",True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

