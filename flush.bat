python manage.py flush --noinput
IF EXIST media\documents\*.* DEL /Q /S media\documents\*.*
python manage.py makemigrations
python manage.py migrate
python manage.py init
python manage.py test app -v 2
python manage.py collectstatic --noinput
python manage.py runserver