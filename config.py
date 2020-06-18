import os 

# set the root directory
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""Parent configuration class"""
	DEBUG = False
	TESTING =False;
	CSRF_ENABLED = True
	SECRET_KEY = "my-secret-key-to-be-set-by-me"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(Config):
	"""Config class for development"""
	DEVELOPMENT = True
	DEBUG = True
		
		
class StageConfig(Config):
	"""Config class for staging the app"""
	DEVELOPMENT = True
	DEBUG = True

class ProConfig(Config):
	"""Config class for main production of the app"""
	DEBUG = False


class ProConfig(Config):
	"""Config class for testing the app"""
	TESTING = True
