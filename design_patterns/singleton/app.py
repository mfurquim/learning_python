#!/bin/env python
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from abc import abstractstaticmethod


class App(ABC):
    def __repr__(self):
        return f"{type(self).__name__} contains: {self.session}"

    def __init__(self, session):
        self.session = session
        self._singleton[0] = self
        print(f"{type(self).__name__}.__init__({self.session})")

    @classmethod
    def current(cls, session: dict):
        """This method retuns the singleton instance."""
        if not cls._singleton[0]:
            return cls(session)
        instance = cls._singleton[0]
        instance.session = session
        return instance

    @abstractmethod
    def abstatic(hoy):
        pass


class FirstApp(App):
    _singleton = [None]

    def abstatic(self, hoy):
        print(f"FirstApp abstatic: {hoy}")


class SecondApp(App):
    _singleton = [None]

    def abstatic(self, hoy):
        print(f"SecondApp abstatic: {hoy}")


class AppManager:
    @staticmethod
    def select_app(device, session):
        source = device.get("source")
        if source == "alternative":
            return SecondApp.current(session)
        elif source == "lite-app" or source == "full-app":
            return FirstApp.current(session)


device = {
    "source": "alternative",
}
session = "sessione"

AppManager.select_app(device, session).abstatic("hoy")


device = {
    "source": "full-app",
}

AppManager.select_app(device, session).abstatic("hola")
