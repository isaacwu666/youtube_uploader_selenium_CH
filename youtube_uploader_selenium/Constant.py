class Constant:
    """A class for storing constants for YoutubeUploader class"""
    NOW_PUBLIC_ID = "checkbox-container"
    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    USER_WAITING_TIME = 1
    VIDEO_TITLE = 'title'
    VIDEO_DESCRIPTION = 'description'
    DESCRIPTION_CONTAINER_ID = 'textbox'
    DESCRIPTION_CONTAINER = '/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/' \
                            'ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]'

    MORE_OPTIONS_CONTAINER = '/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/' \
                             'ytcp-uploads-details/div/div/ytcp-button/div'
    TEXTBOX = 'textbox'
    TEXT_INPUT = 'input'
    RADIO_LABEL = 'radioLabel'
    STATUS_CONTAINER = '/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[2]/' \
                       'div/div[1]/ytcp-video-upload-progress/span'
    NOT_MADE_FOR_KIDS_LABEL = 'NOT_MADE_FOR_KIDS'
    # /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytcp-form-audience/ytcp-audience-picker/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[2]/ytcp-ve

    NOT_MADE_FOR_KIDS_LABEL_CLASS = 'style-scope ytcp-audience-picker'
    NEXT_BUTTON = 'next-button'
    PUBLIC_BUTTON = 'PUBLIC'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'uploaded'
    ERROR_CONTAINER = '//*[@id="error-message"]'
    VIDEO_NOT_FOUND_ERROR = 'Could not find video_id'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
