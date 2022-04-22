#!/bin/env python
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from abc import abstractstaticmethod


class App(ABC):
    def __init__(self, device):
        self.device = device
        print(f"{type(self).__name__}.__init__({self.device})")

    def __repr__(self):
        return f"{type(self).__name__} contains: {self.device}"

    @abstractstaticmethod
    def abstatic(hoy):
        pass


class FirstApp(App):
    def abstatic(hoy):
        print(f"FirstApp abstatic: {hoy}")


class SecondApp(App):
    def abstatic(hoy):
        print(f"SecondApp abstatic: {hoy}")


class FirstAppManagerMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"FirstAppManager.__call__({cls}, {args}, {kwargs})")
        device = kwargs.get("device") or args[0]
        assert isinstance(device, dict)
        source = device.get("source")
        if source == "alternative":
            return SecondApp(*args, **kwargs)
        elif source == "lite-app" or source == "full-app":
            return FirstApp(*args, **kwargs)


class FirstAppManager(metaclass=FirstAppManagerMeta):
    def __init__(self, device):
        self.device = device
        print(f"FirstAppManager.__init__({self.device})")


device = {
    "source": "alternative",
}

first_app = FirstAppManager(device)
print(f"first_app: {first_app}")
SecondApp.abstatic("a")


device = {
    "source": "full-app",
}

second_app = FirstAppManager(device=device)
print(f"second_app: {second_app}")
