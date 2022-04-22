#!/bin/env python


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(f"Singleton.__call__({cls}, {args}, {kwargs})")
        if cls not in cls._instances:
            print(f"cls not in cls._instances")
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class FastLayerManager(metaclass=Singleton):
    def __init__(self, company_id=None):
        print(f"FastLayerManager.__init__({company_id})")
        self._cassandra_client = CassandraClient(company_id)

    def __repr__(self):
        return f"FasLayerManager contains: {self._cassandra_client}"


class CassandraClient:
    def __init__(self, company_id):
        print(f"CassandraClient.__init__({company_id})")
        self._company_id = company_id

    def __repr__(self):
        return f"CassandraClient w/ company_id {self._company_id}"


fast_layer = FastLayerManager("ACompanyID")
print(fast_layer)
fast_layer = FastLayerManager()
print(fast_layer)
