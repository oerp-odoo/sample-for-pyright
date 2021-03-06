from typing import Any

__version_info__: Any
__version__: Any

def user_data_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., roaming: bool = ...): ...
def site_data_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., multipath: bool = ...): ...
def user_config_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., roaming: bool = ...): ...
def site_config_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., multipath: bool = ...): ...
def user_cache_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., opinion: bool = ...): ...
def user_log_dir(appname: Any | None = ..., appauthor: Any | None = ..., version: Any | None = ..., opinion: bool = ...): ...

class AppDirs:
    appname: Any
    appauthor: Any
    version: Any
    roaming: Any
    multipath: Any
    def __init__(self, appname, appauthor: Any | None = ..., version: Any | None = ..., roaming: bool = ..., multipath: bool = ...) -> None: ...
    @property
    def user_data_dir(self): ...
    @property
    def site_data_dir(self): ...
    @property
    def user_config_dir(self): ...
    @property
    def site_config_dir(self): ...
    @property
    def user_cache_dir(self): ...
    @property
    def user_log_dir(self): ...

def _get_win_folder_from_registry(csidl_name): ...
def _get_win_folder_with_pywin32(csidl_name): ...
def _get_win_folder_with_ctypes(csidl_name): ...
_get_win_folder = _get_win_folder_with_pywin32
_get_win_folder = _get_win_folder_with_ctypes
_get_win_folder = _get_win_folder_from_registry
