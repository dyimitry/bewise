FROM python:3.13-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DOCKER_ENV=True

# Добавляем путь к Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Устанавливаем curl
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    echo "Curl installed successfully"

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo "Poetry installed successfully" && \
    poetry --version  # Проверяем, доступна ли Poetry

RUN pip install --upgrade poetry
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Проверяем, доступна ли Poetry
RUN poetry --version

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi -vv
# Копируем остальные файлы проекта в контейнер
COPY . /app

# Создаем пользователя для запуска приложения и меняем владельца файлов
RUN adduser --disabled-password --gecos '' app_user && \
    chown -R app_user:app_user /app

USER app_user

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["/bin/sh", "-c", "export PYTHONPATH=/app && alembic upgrade head &&  uvicorn.run('main:app', reload=True)"]
