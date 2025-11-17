# Тестовое заданние от hitalent

## Развертывание проекта

### Копируем репозиторий
```bash
git clone https://github.com/romich995/hitalent.git
```

### Создаем папку data
```bash
cd ./hitalent
mkdir data
```

### Билдим проект
```bash
docker compose build
```

### Запуск проекта 
```bash
docker compose up
```

### Проводим миграцию 
```bash
docker compose exec web alembic upgrade head
```

### Примеры запросов здесь:
http://127.0.0.1:8000/docs