# Заметки на Django

## Описание

### Что такое заметка?
Заметка — это описание небольшого дела. 
К сожалению, человек не в состоянии удержать все дела в голове, 
поэтому он нередко прибегает к использованию различных средств для
хранения и управления своими заметками.

### Функции веб-приложения
* Создание заметок
* Удаление выполненных заметок
* Хранение всех заметок  

### Доступные страницы (картинки)
1. [Главная страница](https://www.google.com)
2. [Создание страницы](https://www.google.com)
3. [Архив заметок](https://www.google.com)
4. [Админ-панель](https://www.google.com)

## Запуск
### Как запустить по шагам
Скачиваем репозиторий
```bash
git clone https://github.com/Daniil-Solo/To-do-on-Django
```
Переходим в папку проекта
```bash
cd To-do-on-Django
```
Создаем и активируем виртуальное окружение
```bash
python -m venv .venv
venv\Scripts\activate
```
Устанавливаем необходимые библиотеки
```bash
pip install -r requirements.txt
```
Переходи в папку приложения
```bash
cd firstapp
```
Запускаем локально веб-приложение
```bash
python manage.py runserver
```

### Как запустить одним копипастом
Просто скопируйте и вставьте в командную строку
```bash
git clone https://github.com/Daniil-Solo/To-do-on-Django
cd To-do-on-Django
python -m venv .venv
venv\Scripts\activate
pip install -r requirements.txt
cd firstapp
python manage.py runserver
```

## Технологии
### Стек
`Python 3.9`
`Django 4`
`Bootstrap 5`
