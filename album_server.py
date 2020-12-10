import album

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request


@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Кол-во альбомов: {}\n".format(len(album_names))
        result += "Список альбомов {}\n".format(artist)
        result += "\n".join(album_names)
    return result


@route("/albums", method="POST")
def add_album():

    # Если при кастинге поля 'год' возникает ошибка, данные введены неверно
    try:
        new_album = album.Album(
            year=int(request.forms.get("year")),
            artist=request.forms.get("artist"),
            genre=request.forms.get("genre"),
            album=request.forms.get("album")
        )
    except ValueError:
        result = HTTPError(409, 'Incorrect data.')
    else:
        if not album.does_exist(new_album):
            album.add(new_album)
            result = 'User added successfully!'
        else:
            result = 'Such album already exists.'

    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
