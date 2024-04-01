import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv()
print(f"- .env: {find_dotenv()}")
print("- reading dd07modules/fsw_config/config.py")
print(f"- FSW_CONFIG_TYPE: {os.environ.get('FSW_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_json_file:
    # config_json_dict = json.load(env_file)
    config_json_dict = json.load(config_json_file)
        # os.environ["PROJECT_ROOT"] = "/Users/nick/Documents/exFlaskBlueprintFrameworkStarterWithLogin/"


class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = config_json_dict.get('SECRET_KEY')
        
        # Database
        self.MYSQL_USER = config_json_dict.get('MYSQL_USER')
        self.MYSQL_PASSWORD = config_json_dict.get('MYSQL_PASSWORD')
        self.MYSQL_SERVER = config_json_dict.get('MYSQL_SERVER')
        self.MYSQL_DATABASE_NAME = config_json_dict.get('MYSQL_DATABASE_NAME')
        self.MYSQL_DB_URI = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}/{self.MYSQL_DATABASE_NAME}"

        #Email stuff
        self.MAIL_SERVER = config_json_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = config_json_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config_json_dict.get('MAIL_EMAIL')
        self.MAIL_PASSWORD = config_json_dict.get('MAIL_PASSWORD')

        #web Guest
        self.GUEST_EMAIL = config_json_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = config_json_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        #Admin stuff
        self.ADMIN_EMAILS = config_json_dict.get('ADMIN_EMAILS')
        self.REGISTRATION_KEY =config_json_dict.get('REGISTRATION_KEY')
        self.BLS_API_URL = config_json_dict.get('BLS_API_URL')

        # Auxiliary and directories
        self.DB_AUXILIARY = os.environ.get('DB_AUXILIARY')
        self.DIR_LOGS = os.path.join(self.DB_AUXILIARY,"logs")
        self.WEBSITE_FILES = os.path.join(self.DB_AUXILIARY,"website_files")
        self.DIR_WEBSITE_IMAGES = os.path.join(self.WEBSITE_FILES,"website_images")
        self.DIR_WEBSITE_VIDEOS = os.path.join(self.WEBSITE_FILES,"website_videos")
        self.DATABASE_HELPERS = os.path.join(self.DB_AUXILIARY,"database_helpers")
        self.DB_UPLOAD = os.path.join(self.DATABASE_HELPERS,"db_upload")

        #Captcha
        self.SITE_KEY_CAPTCHA = config_json_dict.get('SITE_KEY_CAPTCHA')
        self.SECRET_KEY_CAPTCHA = config_json_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        self.LIST_NO_CONFIRMASTION_EMAILS = config_json_dict.get('LIST_NO_CONFIRMASTION_EMAILS')

class ConfigWorkstation(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        # self.PROJECT_ROOT = os.environ.get('PROJECT_LOCAL_ROOT')

    DEBUG = True


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

    DEBUG = True
    # SQL_URI = config_json_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    # SCHED_CONFIG_STRING = "ConfigDev"
    # CONFIG_TYPE='dev'


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    # SCHED_CONFIG_STRING = "ConfigProd"
    # CONFIG_TYPE='prod'