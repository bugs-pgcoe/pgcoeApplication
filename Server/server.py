import json
import pathlib
from flask import Flask, request, jsonify, render_template


class FileHandler:
    def __init__(self, file_name, create_file=False):
        self._filename = file_name
        self._fw = None
        if (not pathlib.Path(file_name).is_file()) and create_file:
            self._fw = open(self._filename, "w")

    def write_json(self, content):
        if self._fw is None:
            self._fw = open(self._filename, "w")
        if isinstance(content, dict):
            self._fw.write(json.dumps(content, indent=4))

    def read_json(self):
        if self._filename.split(".")[-1].lower() == "json":
            if pathlib.Path(self._filename).is_file():
                try:
                    with open(self._filename, "r") as fr:
                        return json.loads(fr.read())
                except json.JSONDecodeError as E:
                    return {"json_error": E}
                except UnicodeDecodeError as E:
                    return {"json_error": E}
            else:
                return {"json_error": "file not found"}


class Server:
    def __init__(self):
        self._app = Flask(__name__)
        self.components = {}
        self._app.add_url_rule("/", "/", self._index)
        self._app.add_url_rule("/get", "/get", view_func=self._get, methods=["GET"])

    def _index(self):
        return render_template("index.html", components=self.components)

    def _get(self):
        res = {}
        for k, v in request.args.items():
            res.update(
                {k : FileHandler(f"config/custom/{v}.json").read_json()}
            )
        return res

    def start(self):
        self._app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    server = Server()
    server.components = {'layout': 'layout', 'table': 'table'}
    server.start()
