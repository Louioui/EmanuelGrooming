#settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',   # Replace 'your_database_name' with your actual database name
        'USER': 'your_database_user',   # Replace 'your_database_user' with your actual database username
        'PASSWORD': 'your_database_password',  # Replace 'your_database_password' with your actual database password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    # Other apps...
    'Grooming',  # Replace 'Grooming' with the name of your Django app
]

# Other settings...
