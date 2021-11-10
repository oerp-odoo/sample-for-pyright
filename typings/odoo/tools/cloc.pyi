from typing import Any

VERSION: int
DEFAULT_EXCLUDE: Any
STANDARD_MODULES: Any
MAX_FILE_SIZE: Any

class Cloc:
    modules: Any
    code: Any
    total: Any
    errors: Any
    max_width: int
    def __init__(self) -> None: ...
    def parse_xml(self, s): ...
    def parse_py(self, s): ...
    def parse_js(self, s): ...
    def book(self, module, item: str = ..., count=...) -> None: ...
    def count_path(self, path, exclude: Any | None = ...) -> None: ...
    def count_modules(self, env) -> None: ...
    def count_customization(self, env) -> None: ...
    def count_env(self, env) -> None: ...
    def count_database(self, database) -> None: ...
    def report(self, verbose: bool = ..., width: Any | None = ...): ...