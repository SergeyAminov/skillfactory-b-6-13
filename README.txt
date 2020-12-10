Запуск локального сервера осуществляется с помощью команды:

python album_server.py

В качестве тестовой операции в базу данных albums.sqlite3 была добавлена следующая запись через терминал:

http -f POST http://localhost:8080/albums year=1970 artist="New Artist" genre="Rock" album="Super"