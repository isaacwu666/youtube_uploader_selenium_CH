"""This module implements uploading videos on YouTube via Selenium using metadata JSON file
    to extract its title, description etc."""

from typing import DefaultDict, Optional
from selenium_firefox.firefox import Firefox
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # 键盘

from collections import defaultdict
import json
import time
from .Constant import *
from pathlib import Path
import logging

logging.basicConfig()


def load_metadata(metadata_json_path: Optional[str] = None) -> DefaultDict[str, str]:
    if metadata_json_path is None:
        return defaultdict(str)
    with open(metadata_json_path) as metadata_json_file:
        return defaultdict(str, json.load(metadata_json_file))


class YouTubeUploader:
    """A class for uploading videos on YouTube via Selenium using metadata JSON file
    to extract its title, description etc"""

    # def __init__(self, video_path: str, metadata_json_path: Optional[str] = None) -> None:
    #     self.video_path = video_path
    #     self.metadata_dict = load_metadata(metadata_json_path)
    #     # current_working_dir = str(Path.cwd())
    #     current_working_dir = "C:\\Users\\isaac\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vczuw9pi.default-release"
    #     self.browser = Firefox(current_working_dir, current_working_dir)
    #     self.logger = logging.getLogger(__name__)
    #     self.logger.setLevel(logging.DEBUG)
    #     self.__validate_inputs()

    def __init__(self, cus_profile_dir, executable_path, service_log_path) -> None:
        self.video_path = None
        self.metadata_dict = None

        # cus_profile_dir = "C:\\Users\\isaac\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\vczuw9pi.default-release"  # 你自定义profile的路径
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(cus_profile_dir)
        option = webdriver.FirefoxOptions()
        # 无头模式
        # option.add_argument("-headless")
        # 禁止加载图片
        option.set_preference('permissions.default.image', 2)
        # 禁止加载css样式表
        option.set_preference('permissions.default.stylesheet', 2)

        # 设置页面加载超时，超过这个时间就会抛出异常，执行以后的代码，否则会卡在>一直加载

        self.browser = webdriver.Firefox(executable_path=executable_path,
                                         firefox_profile=profile,
                                         options=option
                                         , service_log_path=service_log_path
                                         )

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.__validate_inputs()

    def __validate_inputs(self):
        # if not self.metadata_dict[Constant.VIDEO_TITLE]:
        #     self.logger.warning("The video title was not found in a metadata file")
        #     self.metadata_dict[Constant.VIDEO_TITLE] = Path(self.video_path).stem
        #     self.logger.warning("The video title was set to {}".format(Path(self.video_path).stem))
        # if not self.metadata_dict[Constant.VIDEO_DESCRIPTION]:
        #     self.logger.warning("The video description was not found in a metadata file")

        pass

    def upload(self, video_path, metadata_json_path):

        try:
            self.__login()
            return self.__upload(video_path, metadata_json_path)
        except Exception as e:
            print(e)
            self.__quit()
            raise

    def __login(self):
        try:
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.get(Constant.YOUTUBE_URL)
            time.sleep(Constant.USER_WAITING_TIME)
        except BaseException as e:
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.get(Constant.YOUTUBE_URL)

            pass

        return
        try:
            res = self.browser.has_cookies_for_current_website()
        except BaseException as e:
            res = True
            print(e)
            pass

        if res:
            self.browser.load_cookies()
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.refresh()
        else:
            self.logger.info('Please sign in and then press enter')
            input()
            self.browser.get(Constant.YOUTUBE_URL)
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.save_cookies()

    def __upload(self, video_path: str, metadata_json_path: Optional[str] = None) -> (bool, Optional[str]):
        metadata_dict = load_metadata(metadata_json_path)

        self.browser.get(Constant.YOUTUBE_URL)
        time.sleep(Constant.USER_WAITING_TIME)
        self.browser.get(Constant.YOUTUBE_UPLOAD_URL)
        time.sleep(Constant.USER_WAITING_TIME)
        absolute_video_path = str(Path.cwd() / video_path)
        try:
            time.sleep(Constant.USER_WAITING_TIME)
            time.sleep(Constant.USER_WAITING_TIME)
            self.browser.find_element(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(absolute_video_path)
            self.logger.debug('Attached video {}'.format(video_path))
            time.sleep(Constant.USER_WAITING_TIME)
            time.sleep(Constant.USER_WAITING_TIME)
            time.sleep(Constant.USER_WAITING_TIME)
            time.sleep(Constant.USER_WAITING_TIME)
            title_field = self.browser.find_element(By.ID, Constant.TEXTBOX)
            time.sleep(Constant.USER_WAITING_TIME)
            title_field.click()
            time.sleep(Constant.USER_WAITING_TIME)
            title_field.clear()
            time.sleep(Constant.USER_WAITING_TIME)
            title_field.send_keys(Keys.COMMAND + 'a')
            time.sleep(Constant.USER_WAITING_TIME)
            title_field.send_keys(metadata_dict[Constant.VIDEO_TITLE])

            time.sleep(Constant.USER_WAITING_TIME)
            time.sleep(Constant.USER_WAITING_TIME)
            self.logger.debug('The video title was set to \"{}\"'.format(metadata_dict[Constant.VIDEO_TITLE]))
        except BaseException as e:
            print(e)
            time.sleep(Constant.USER_WAITING_TIME)
        pass
        video_description = metadata_dict[Constant.VIDEO_DESCRIPTION]
        video_description = False
        if video_description:
            # 视频介绍

            time.sleep(Constant.USER_WAITING_TIME)

            description_field = self.browser.find_element(By.ID, Constant.TEXT_INPUT)
            description_field.click()
            time.sleep(Constant.USER_WAITING_TIME)
            description_field.clear()
            time.sleep(Constant.USER_WAITING_TIME)
            description_field.send_keys(metadata_dict[Constant.VIDEO_DESCRIPTION])
            self.logger.debug(
                'The video description was set to \"{}\"'.format(metadata_dict[Constant.VIDEO_DESCRIPTION]))
            time.sleep(Constant.USER_WAITING_TIME)

        try:
            time.sleep(Constant.USER_WAITING_TIME)
            kids_section = self.browser.find_element(By.NAME, Constant.NOT_MADE_FOR_KIDS_LABEL)
        except BaseException as e:
            print("NOT_MADE_FOR_KIDS_LABEL", e)
            time.sleep(Constant.USER_WAITING_TIME)
            kids_section = self.browser.find_element(By.CLASS_NAME, Constant.NOT_MADE_FOR_KIDS_LABEL_CLASS)
            pass
        time.sleep(Constant.USER_WAITING_TIME)
        try:

            kids_section = self.browser.find_element(By.NAME, Constant.NOT_MADE_FOR_KIDS_LABEL).click()
            self.logger.debug('Selected \"{}\"'.format(Constant.NOT_MADE_FOR_KIDS_LABEL))
        except BaseException as e:
            print(e)
            pass
        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)

        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked {}'.format(Constant.NEXT_BUTTON))

        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)

        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked another {}'.format(Constant.NEXT_BUTTON))

        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)

        self.browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
        self.logger.debug('Clicked another {}'.format(Constant.NEXT_BUTTON))

        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)
        public_main_button = self.browser.find_element(By.NAME, Constant.PUBLIC_BUTTON).click()

        time.sleep(Constant.USER_WAITING_TIME)
        time.sleep(Constant.USER_WAITING_TIME)

        try:
            self.browser.find_element(By.ID, Constant.NOW_PUBLIC_ID).click()
        except BaseException as e:
            print("设置为及时首映错误", e)
            pass

        # self.browser.find_element(By.ID, Constant.RADIO_LABEL, public_main_button).click()
        self.logger.debug('Made the video {}'.format(Constant.PUBLIC_BUTTON))

        video_id = self.__get_video_id()
        start_time = time.time()
        while True:
            if self.__get_uploading():
                time.sleep(Constant.USER_WAITING_TIME)
            else:
                if time.time() - start_time > 15 * 60:
                    print("等待超过15分钟,不等了，直接上传")
                    break
                    pass
                break
        pass

        done_button = self.browser.find_element(By.ID, Constant.DONE_BUTTON)

        # Catch such error as
        # "File is a duplicate of a video you have already uploaded"
        if done_button.get_attribute('aria-disabled') == 'true':
            error_message = self.browser.find_element(By.XPATH,
                                                      Constant.ERROR_CONTAINER).text
            self.logger.error(error_message)
            return False

        done_button.click()
        self.logger.debug("Published the video with video_id = {}".format(video_id))
        time.sleep(Constant.USER_WAITING_TIME)
        self.browser.get(Constant.YOUTUBE_URL)
        self.__quit()
        return True

    def __get_uploading(self) -> bool:
        try:
            self.browser.find_element(By.XPATH, "//*[contains(.,'检查完毕。未发现任何问题。')]")

        except BaseException as e:
            print("e", e)
            return True
            pass
        return False
        pass

    def __get_video_id(self) -> Optional[str]:
        video_id = None
        try:
            video_url_container = self.browser.find_element(By.XPATH, Constant.VIDEO_URL_CONTAINER)
            video_url_element = self.browser.find_element(By.XPATH, Constant.VIDEO_URL_ELEMENT,
                                                          element=video_url_container)
            video_id = video_url_element.get_attribute(Constant.HREF).split('/')[-1]
        except:
            self.logger.warning(Constant.VIDEO_NOT_FOUND_ERROR)
            pass
        return video_id

    def __quit(self):
        return
        self.browser.quit()
        pass
