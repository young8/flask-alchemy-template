class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SEND_FILE_MAX_AGE_DEFAULT = 300


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'