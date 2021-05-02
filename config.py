import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/quickhowto'
#SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost:5432/myapp'
#SQLALCHEMY_ECHO = True

BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_FOLDER = 'translations'
LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    'pt': {'flag':'pt', 'name':'Portuguese'},
    'pt_BR' : {'flag':'br', 'name':'Pt Brasil'},
    'es': {'flag':'es', 'name':'Spanish'},
    'de': {'flag':'de', 'name':'German'},
    'zh': {'flag':'cn', 'name':'Chinese'},
    'ru': {'flag':'ru', 'name':'Russian'},
    'pl': {'flag':'pl', 'name':'Polish'}
}



#------------------------------
# GLOBALS FOR GENERAL APP's
#------------------------------
UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'
AUTH_TYPE = 1
#AUTH_LDAP_SERVER = "ldap://dc.domain.net"
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
RECAPTCHA_PUBLIC_KEY = '6LetusIaAAAAAPNkqm6SPdz8atD3cjk7FVF3FWoy'
RECAPTCHA_PRIVATE_KEY = '6LetusIaAAAAANi9MBjsRv1sM7zcfhmztDTJSpWH'
AUTH_ROLE_PUBLIC = 'Public'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_TLS = True
MAIL_USERNAME = 'yourappemail@gmail.com'
MAIL_PASSWORD = 'passwordformail'
MAIL_DEFAULT_SENDER = 'fabtest10@gmail.com'
APP_NAME = "Apple"
APP_THEME = ""                  # default
#APP_THEME = "cerulean.css"      # COOL
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"       # COOL
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"          # COOL
#APP_THEME = "spacelab.css"      # NICE
#APP_THEME = "united.css"
