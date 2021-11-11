FLASK_ENV=development
FLASK_APP=real_price.app:create_app
SECRET_KEY=changeme
DATABASE_URI=sqlite:///real_price.db
CELERY_BROKER_URL=amqp://guest:guest@localhost/
CELERY_RESULT_BACKEND_URL=rpc://
