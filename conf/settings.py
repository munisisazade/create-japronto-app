
# Japronto by Munis Isazade

import os
import firebase_admin
from firebase_admin import credentials

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/code/firebase/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://munis-b4ec6.firebaseio.com/',
    'storageBucket': 'munis-b4ec6.appspot.com/'
})

SECRET_KEY = "Kcb8yBVBymbwSe4NHEdu9RsM6rrBVQLtSMredaFAnEW3IOFfhIxgnQQj58KOMk5sWkxYk2o"

DEBUG = True

PORT = 8050

BASE_DIR = '/code'
TEMP_DIR = BASE_DIR + '/base_application/templates/'

from base_application.urls import munis