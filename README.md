# currency_converter



![тестовое.jpg](%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5.jpg)


1. В файле settings.py добавьте свой API-ключ, 
который можно получить, зарегистрировавшись на сайте:
https://openexchangerates.org/

2. pip install -r requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

POST /api/convert/
```
{
    "base_currency": "USD",
    "target_currency": "EUR",
    "amount": 100
}
```
