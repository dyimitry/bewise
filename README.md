Для запуска и коректной работы  приложения необходимо собрать образ и на его основе запустить контейнер.
Также необходимо  будет примонтировать данные из .env файла

Создание образа производится командой:
docker build -t <name_image> .   

Поднять контейнеры: 
docker compose up  


В приложение имеются 2 ручки:
1. создать заявку

Примеры: 
POST /applications Create Application
{
  "user_name": "vasek",
  "description": "xochet"
}


Code	Details
200	
Response body
Download
{
  "id": 26,
  "user_name": "vasek",
  "description": "xochet",
  "created_at": "2025-01-19T01:16:48.309618"
}

2. показать список созданных заявок
GET /applications Get Applications

[
  {
    "id": 0,
    "user_name": "string",
    "description": "string",
    "created_at": "2025-01-16T14:43:48.150000"
  },
  {
    "id": 1,
    "user_name": "string",
    "description": "string",
    "created_at": "2025-01-16T17:52:08.439128"
  },
  {
    "id": 2,
    "user_name": "string",
    "description": "string",
    "created_at": "2025-01-16T17:52:14.788417"
  },
  {
    "id": 3,
    "user_name": "string",
    "description": "string",
    "created_at": "2025-01-16T17:52:18.866602"
  }
]