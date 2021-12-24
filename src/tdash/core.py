from typing import ClassVar


class TComponent:
    name: ClassVar[str] = 'component'

    def build_id(self, *args: str) -> str:
        return f"{self.name}{''.join([f'-{x}' for x in args])}"

    def build_children_id(self, *args: str) -> str:
        return f"{self.build_id()}{''.join([f'-{x}' for x in args])}"

    def build_children(self):
        pass
