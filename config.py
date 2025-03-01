import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base configuration class
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
    TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    SMTP_SERVER = os.environ.get('SMTP_SERVER') or 'smtp.gmail.com'
    SMTP_PORT = int(os.environ.get('SMTP_PORT') or 587)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'leadbot@example.com'
    SCHEDULER_ENABLED = os.environ.get('SCHEDULER_ENABLED', 'True') == 'True'
    CACHE_DIR = 'cache'
    
    # Google Cloud specific config
    PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT')
    
    # Social media platforms to search (comma-separated)
    SEARCH_PLATFORMS = os.environ.get('SEARCH_PLATFORMS', 'twitter,linkedin').split(',')
    
    # Default search parameters
    DEFAULT_SEARCH_PARAMS = {
        "location": os.environ.get('DEFAULT_LOCATIONS', 'San Francisco,New York').split(','),
        "max_age_days": int(os.environ.get('DEFAULT_MAX_AGE_DAYS', 30)),
        "seniority_levels": os.environ.get('DEFAULT_SENIORITY_LEVELS', 'executive,senior').split(','),
        "company_size": {
            "min": int(os.environ.get('DEFAULT_MIN_COMPANY_SIZE', 50)),
            "max": int(os.environ.get('DEFAULT_MAX_COMPANY_SIZE', 500))
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True
    # Use local emulators for Firestore when in development
    os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8080'


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


# Default to development config
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# Set the active configuration
active_config = config[os.environ.get('FLASK_ENV', 'default')]()