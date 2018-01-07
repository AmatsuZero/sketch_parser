from zipfile import ZipFile
from os import path
import json as js
from pprint import pprint

testPath = "~/Desktop/test/sample.sketch"


def json(zip_file, file):
    name = file.filename
    content = js.loads(zip_file.read(name))
    pprint(content)


def png(zip_file, file):
    pass


handler = {
    '.json': json,
    '.png': png
}


def unzip_sketch_file(name):
    sketch = ZipFile(name)
    for file in sketch.infolist():
        ext = path.splitext(file.filename)[1]
        handler[ext](sketch, file)
    sketch.close()


if __name__ == "__main__":
    sketchPath = path.expanduser(testPath)
    unzip_sketch_file(sketchPath)
