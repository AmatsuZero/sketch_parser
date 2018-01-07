from zipfile import ZipFile
from os import path
import json as js
from picture_hook import save_image
from document_hook import DocumentObject

testPath = "./assets/sample.sketch"


def json(zip_file, file):
    with zip_file.open(file, 'r') as JSON:
        document = js.load(JSON, object_hook=DocumentObject)


def png(zip_file, file):
    with zip_file.open(file, 'r') as pic:
        save_image(pic)


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
