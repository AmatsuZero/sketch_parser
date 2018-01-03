from zipfile import ZipFile
from os import path
import json

testPath = "~/Desktop/test/sample.sketch"


def json(file):
    content = json.load(file)
    print(content)


def png(file):
    print(file)


handler = {
    '.json': json,
    '.png': png
}


def unzip_sketch_file(name):
    sketch = ZipFile(name)
    for file in sketch.infolist():
        ext = path.splitext(file.filename)[1]
        handler[ext](file)
    sketch.close()


if __name__ == "__main__":
    sketchPath = path.expanduser(testPath)
    unzip_sketch_file(sketchPath)
