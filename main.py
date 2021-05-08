import argparse
import time

from youtube_uploader_selenium import YouTubeUploader
from typing import Optional

if __name__ == "__main__":
    # 你自定义profile的路径 ，提前登录然后在使用
    cus_profile_dir = "C:\\Users\\isaac\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vczuw9pi.default-release"
    # geckodriver 路径
    executable_path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"
    # 日志输出文件，必须保证目录存在，
    service_log_path = "G:\\tmp\\foxwatch.log"
    # 创建上传对象
    uploader = YouTubeUploader(cus_profile_dir, executable_path, service_log_path)
    while True:

        try:
            # 执行上传
            uploader.upload(".\\test.mp4", ".\\健身的国外美女图片_17.json")
            break
        except BaseException as e:
            print("uploader.upload:", e)
            time.sleep(20)
            pass

    pass
