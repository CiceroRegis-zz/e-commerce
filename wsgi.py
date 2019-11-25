from whitenoise.django import DjangoWhiteNoise

web: gunicorn ecommerce.wsgi --log-file -
application = DjangoWhiteNoise(application)