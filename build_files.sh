echo "BUILD START"
python3.12.4 -m pip install -r requirements.txt
python3.12.4 manage.py collectstatic
echo "BUILD END"
