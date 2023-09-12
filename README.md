# Проект API для YaTube

![Python](https://img.shields.io/badge/Python-313131?style=flat&logo=Python&logoColor=white&labelColor=306998)
![Django](https://img.shields.io/badge/Django-313131?style=flat&logo=django&labelColor=092e20)
![DjangoREST](https://img.shields.io/badge/Django-REST-313131?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=313131)
![Visual Studio](https://img.shields.io/badge/VS%20Code-313131?style=flat&logo=visualstudiocode&logoColor=ffffff&labelColor=0098FF)

## Проект является API для платформы Yatube, который позволяет запрашивать данные о постах, группах, комментариях и подписках.

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/deltabobkov/api_final_yatube.git

cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env

source env/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Запустить проект:

```
python manage.py runserver
```
