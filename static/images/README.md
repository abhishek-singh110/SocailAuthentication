# Django Project with Social Login

This project is a Django application that includes social login functionality with Google and Facebook. It allows users to sign in using their social media accounts.

## Features

- User registration and authentication
- Social login with Google
- Social login with Facebook

## Technologies Used

- Django
- Python
- HTML
- CSS
- Social-auth-app-django

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**

    ```bash
    python manage.py runserver
    ```

## Configuration

### Google Social Login

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project.
3. Navigate to the "OAuth consent screen" and configure your application.
4. Navigate to "Credentials" and create an OAuth 2.0 Client ID.
5. Add the Client ID and Client Secret to your Django settings:

    ```python
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'
    ```

### Facebook Social Login

1. Go to the [Facebook Developers](https://developers.facebook.com/apps/?show_reminder=true) website.
2. Login you facebook account.
3. Create a new app.
4. In Business Portfolio -> click on next
5. In Use Cases -> select the "Authenticate and request data from users with Facebook Login".
6. In App Detials -> add you app name and email.
7. Review and created.
8. Go to App Setting >> Basic - copy the App ID and App Secret.
9. ADD -:
   - App domain -> localhost
   - Privacy Policy URL -> http://127.0.0.1:8000/
10. Click on Add Platform and choose the website, in Site URL add http://localhost:8000/

    ```python
    SOCIAL_AUTH_FACEBOOK_KEY = 'your-facebook-app-id'
    SOCIAL_AUTH_FACEBOOK_SECRET = 'your-facebook-app-secret'
    ```

### Update Django Settings

Add the following configurations to your `settings.py`:

```python
AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    'authentication.backends.EmailBackend', 
]

INSTALLED_APPS += (
    'social_django',
    'django.contrib.sites',
    
)

MIDDLEWARE += (
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
)

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"

# Google OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'

# Facebook OAuth2 settings
SOCIAL_AUTH_FACEBOOK_KEY = 'your-facebook-app-id'
SOCIAL_AUTH_FACEBOOK_SECRET = 'your-facebook-app-secret'
