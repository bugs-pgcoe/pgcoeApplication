import json
import pathlib


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


class UICreator:
    def __init__(self):
        self._component = {
            "children": [

            ]
        }


    def create_layout(self, id):
        layout = {
                "div": {
                    "class": "container-fluid",
                    "id": id,
                    "style": "height: 100vh;width: 100hw",
                    "children": []
                }
            }
        self._component["children"].append(
            layout
        )
        _index = self._component["children"].index(layout)
        return self._component["children"][_index]["div"]["children"]

    def add_row(self, component, id):
        row = {
            "div": {
                "class": "row",
                "id": id,
                "style": "width:100hw;height:10%;margin:2px;position:relative;top:2px",
                "children": [
                ]
            }
        }
        component.append(row)
        _index = component.index(row)
        return component[_index]["div"]["children"]

    def add_column(self, component, id):
        col = {
            "div": {
                "class": "col",
                "id": id,
                "style": "width:100hw;height:10%;margin:2px;position:relative;top:2px",
                "children": [
                ]
            }
        }
        component.append(col)
        _index = component.index(col)
        return component[_index]["div"]["children"]

    def get_component(self):
        return self._component

    def write_component(self, file, component):
        FileHandler(file).write_json(component)



if __name__ == "__main__":
    obj = UICreator()
    layout = obj.create_layout("main-container1")
    row = obj.add_row(layout, "header-row1")
    col = obj.add_column(row, "header-row1-col1")
    col = obj.add_column(row, "header-row1-col2")
    row = obj.add_row(col, "header-row1-col2-row1")
    col = obj.add_column(row, "header-row1-col2-row1-col1")
    col = obj.add_column(row, "header-row1-col2-row1-col2")
    row = obj.add_row(layout, "header-row2")
    col = obj.add_column(row, "header-row2-col1")
    col = obj.add_column(row, "header-row2-col2")

    FileHandler("layout.json").write_json(obj.get_component())