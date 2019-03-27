# CasaRonaldMcDonald
Proyecto con fines educativos para [Fundación Infantil Ronald McDonald (FIRM)](https://www.firmguatemala.org). Construido con **Django**.

Principalmente es un sistema administrativo para casas, pacientes e información (blog, eventos, etc).
Este sistema también despligue la página para usuarios normales donde pueden ver información sobre
las casas, eventos, blog.

## Requisitos
+ python3.5+
+ pipenv

## Instalación

* `git clone https://github.com/foursquarex/CasaRonaldMcDonald`
* `cd CasaRonaldMcDonald/ronald`
* `pipenv install`

## Servidor de desarrollo

* `python manage.py collectstatic --no-input`
* `python manage.py runserver`
