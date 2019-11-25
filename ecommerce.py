from whitenoise.django import DjangoWhiteNoise

web: gunicorn ecommerce.wsgi --log-file -
web: bundle exec rails server -p $PORT
application = DjangoWhiteNoise(application)