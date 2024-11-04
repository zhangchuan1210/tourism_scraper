# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'hive://root:123456@172.31.11.61:10000/default?auth=CUSTOM'  # Hive 连接字符串
    SQLALCHEMY_TRACK_MODIFICATIONS = False
