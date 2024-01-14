FROM python:3.10.5

# Установка переменной среды
ENV PYTHONUNBUFFERED 1

# Создание директории приложения
RUN mkdir /app

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей файла
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование приложения в контейнер
COPY . /app/

# Открытие порта 8000
EXPOSE 8000

# Запуск команды приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
