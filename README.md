# Тестовое задание  
### Тестовое задание для разработчиков SRE (FunBox)

*Стек:  
Python:3.10,  
aiohttp:3.8.5,  
Pydantic:2.3.0*

### Описание скриптов

logreader.py - считывает файл [events.log](events.log) и выводит в консоль число событий NOK за каждую минуту.  
server_poll.py - ежеминутно опрашивает сервера по списку и выводит в консоль полученную при опросе метрику рядом с названием сервера.

### Запуск скриптов

---
1. Установить зависимости:
```python
pip install -r requirements.txt
```
2. Запустить скрипты:

```python
python logreader.py
```

```python
python server_poll.py
```