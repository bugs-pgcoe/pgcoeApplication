import json

from flask import Flask, request, jsonify, render_template
from template_generator import FileHandler


class Server:
    def __init__(self):
        self._app = Flask(__name__)
        self._app.add_url_rule("/", "/", self._index)
        self._app.add_url_rule("/post", "/post", view_func=self._post, methods=["POST"])

    def _index(self):
        return render_template("index.html", templates={"templates": FileHandler("template_.json").read_json()},
                               test_table_data=json.dumps((FileHandler("table_data.json").read_json())))

    def _post(self):
        mapping = {
            "templates": "template_.json"
        }
        for k, v in request.json.items():
            FileHandler(mapping.get(k)).write_json(request.json)
        return "success"

    def start(self):
        self._app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    server = Server()
    server.start()
