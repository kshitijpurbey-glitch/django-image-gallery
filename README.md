# Django Image Gallery

A Django image gallery based on the GeeksforGeeks **Image Gallery GUI using Django** tutorial, with improved styling, sample images, fixture data and project documentation.

## Features
- Image gallery using Django `ImageField`
- SQLite database
- Admin panel for adding/managing images
- Responsive UI
- Included sample images and fixture

## Run locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata gallery/fixtures/sample_products.json
python manage.py createsuperuser
python manage.py runserver
```

Open **http://127.0.0.1:8000/** for the gallery and **http://127.0.0.1:8000/admin/** for management.

## Project structure
```text
gallery/
  fixtures/
  migrations/
  static/gallery/
  templates/gallery/
  admin.py models.py urls.py views.py
imagegallery/
manage.py
media/products/
requirements.txt
README.md
```

## Sample data
Three sample images are included in `media/products/`. Load their database records with:
```bash
python manage.py loaddata gallery/fixtures/sample_products.json
```

## Source
Concept adapted from:
https://www.geeksforgeeks.org/python/image-gallery-gui-using-django/
