import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    USER_NAME: str = os.environ.get('USER_NAME')
    ACCESS_KEY: str = os.environ.get('ACCESS_KEY')

    deviceName_android: str = 'Samsung Galaxy S22 Ultra'
    platformVersion_android: str = '12.0'
    deviceName_ios: str = 'iPhone 13'
    platformVersion_ios: str = '15'
    app: str = 'bs://sample.app'
    timeout: float = 10.0


settings = Settings()
