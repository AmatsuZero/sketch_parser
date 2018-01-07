from pprint import pprint


class DocumentObject:
    def __init__(self, d):
        self.__dict__ = d
