mm:
	sudo docker compose run web python manage.py makemigrations
mg:
	sudo docker compose run web python manage.py migrate 

