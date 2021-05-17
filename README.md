## About

原项目地址：https://github.com/linouk23/youtube_uploader_selenium
<br>如果发现这个项目无法使用，可以去看看原项目，说不定又可以了。<br>
在使用时发现无法正常使用，于是进行了一些‘小小的’改动，因为即使是这小小的改动代码也全部面目全非了，但是保证了最基础的使用，目前正常使用中，每天都可以水油管的视频，爽的一匹。

## 使用方式
参考 main.py
```
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
    
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
