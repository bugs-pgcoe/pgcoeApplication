import json
import pathlib
from flask import Flask, request, jsonify, render_template


class FileHandler:
    def __init__(self, file_name):
        self._filename = file_name
        self._fw = None
        if not pathlib.Path(file_name).is_file():
            self._fw = open(self._filename, "w")

    def write_json(self, content):
        if self._fw is None:
            self._fw = open(self._filename, "w")
        if isinstance(content, dict):
            self._fw.write(json.dumps(content, indent=4))

    def read_json(self):
        if self._filename.split(".")[-1].lower() == "json":
            try:
                with open(self._filename, "r") as fr:
                    return json.loads(fr.read())
            except json.JSONDecodeError as E:
                return {"json_error": E}
            except UnicodeDecodeError as E:
                return {"json_error": E}


class Server:
    def __init__(self):
        self._app = Flask(__name__)
        self._app.add_url_rule("/", "/", self._index)
        self._app.add_url_rule("/post", "/post", view_func=self._post, methods=["POST"])

    def _index(self):
        return render_template("index.html")

    def _post(self):
        return "success"

    def start(self):
        self._app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    server = Server()
    server.start()
