class TComponent:
    name: str = 'component'

    def build_id(self, *args) -> str:
        return f"{self.name}{''.join([f'-{x}' for x in args])}"
