import os
class Config:
   
    SQLALCHEMY_TRACK_MODIFICATIONS = True
 
class ProdConfig:
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
class DevConfig:
    DEBUG = True
config_options={
'development':DevConfig,
'production':ProdConfig

}
