pip install -r requirements.txt
pip install --upgrade pip
pip install pysqlite3
python3 manage.py collectstatic
python3 manage.py runserver