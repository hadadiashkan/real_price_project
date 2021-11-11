FLASK_ENV=development
FLASK_APP=real_price.app:create_app
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
