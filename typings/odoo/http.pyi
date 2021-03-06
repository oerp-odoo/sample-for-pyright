from typing import Any, Union

import werkzeug.wrappers

from .api import Environment
from .modules.registry import Registry
from .sql_db import Cursor
from .tools._vendor import sessions

_logger: Any
rpc_request: Any
rpc_response: Any
STATIC_CACHE: Any
STATIC_CACHE_LONG: Any
ALLOWED_DEBUG_MODES: Any
_request_stack: Any
request: Union[HttpRequest, JsonRequest]

def replace_request_password(args): ...

NO_POSTMORTEM: Any

def dispatch_rpc(service_name, method, params): ...

class WebRequest:
    httprequest: werkzeug.wrappers.Request
    httpresponse: Response
    disable_db: bool
    endpoint: Any
    endpoint_arguments: Any
    auth_method: Any
    website = Environment['website']
    _cr: Cursor
    _uid: int
    _context: dict
    _env: Environment
    _failed: Any
    def __init__(self, httprequest) -> None: ...
    @property
    def cr(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, val) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, val) -> None: ...
    @property
    def env(self) -> Environment: ...
    @property
    def session(self) -> OpenERPSession: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def set_handler(self, endpoint, arguments, auth) -> None: ...
    def _handle_exception(self, exception) -> None: ...
    def redirect(self, location, code: int = ..., local: bool = ...): ...
    def redirect_query(self, location, query: Any | None = ..., code: int = ..., local: bool = ...): ...
    def _is_cors_preflight(self, endpoint): ...
    def _call_function(self, *args, **kwargs): ...
    def registry_cr(self) -> None: ...
    @property
    def registry(self) -> Registry: ...
    @property
    def db(self): ...
    def csrf_token(self, time_limit: Any | None = ...): ...
    def validate_csrf(self, csrf): ...

def route(route: Any | None = ..., **kw): ...

class JsonRequest(WebRequest):
    _request_type: str
    params: Any
    jsonrequest: Any
    context: Any
    def __init__(self, *args) -> None: ...
    def _json_response(self, result: Any | None = ..., error: Any | None = ...): ...
    def _handle_exception(self, exception): ...
    def dispatch(self): ...

def serialize_exception(e): ...

class HttpRequest(WebRequest):
    _request_type: str
    params: Any
    def __init__(self, *args) -> None: ...
    def _handle_exception(self, exception): ...
    def _is_cors_preflight(self, endpoint): ...
    def dispatch(self): ...
    def make_response(self, data, headers: Any | None = ..., cookies: Any | None = ...): ...
    def render(self, template, qcontext: Any | None = ..., lazy: bool = ..., **kw): ...
    def not_found(self, description: Any | None = ...): ...

addons_manifest: Any
controllers_per_module: Any

class ControllerType(type):
    def __init__(cls, name, bases, attrs) -> None: ...

Controller: Any

class EndPoint:
    method: Any
    original: Any
    routing: Any
    arguments: Any
    def __init__(self, method, routing) -> None: ...
    @property
    def first_arg_is_req(self): ...
    def __call__(self, *args, **kw): ...

def _generate_routing_rules(modules, nodb_only, converters: Any | None = ...): ...

class AuthenticationError(Exception): ...
class SessionExpiredException(Exception): ...

class OpenERPSession(sessions.Session):
    inited: bool
    modified: bool
    rotate: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, k, v): ...
    pre_uid: Any
    db: Any
    login: Any
    def authenticate(self, db, login: Any | None = ..., password: Any | None = ...): ...
    session_token: Any
    def finalize(self) -> None: ...
    def check_security(self) -> None: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    def _default_values(self) -> None: ...
    context: Any
    def get_context(self): ...
    def _fix_lang(self, context) -> None: ...
    def save_action(self, action): ...
    def get_action(self, key): ...
    def save_request_data(self) -> None: ...
    def load_request_data(self) -> None: ...

def session_gc(session_store) -> None: ...

ODOO_DISABLE_SESSION_GC: Any
session_gc: Any

class Response(werkzeug.wrappers.Response):
    default_mimetype: str
    def __init__(self, *args, **kw) -> None: ...
    template: Any
    qcontext: Any
    uid: Any
    def set_default(self, template: Any | None = ..., qcontext: Any | None = ..., uid: Any | None = ...) -> None: ...
    @property
    def is_qweb(self): ...
    def render(self): ...
    def flatten(self) -> None: ...

class DisableCacheMiddleware:
    app: Any
    def __init__(self, app) -> None: ...
    def __call__(self, environ, start_response): ...

class Root:
    _loaded: bool
    def __init__(self) -> None: ...
    def session_store(self): ...
    def nodb_routing_map(self): ...
    def __call__(self, environ, start_response): ...
    def load_addons(self) -> None: ...
    def setup_session(self, httprequest): ...
    def setup_db(self, httprequest) -> None: ...
    def setup_lang(self, httprequest) -> None: ...
    def get_request(self, httprequest): ...
    def get_response(self, httprequest, result, explicit_session): ...
    def dispatch(self, environ, start_response): ...
    def get_profiler_context_manager(self, request): ...
    def get_db_router(self, db): ...

def db_list(force: bool = ..., httprequest: Any | None = ...): ...
def db_filter(dbs, httprequest: Any | None = ...): ...
def db_monodb(httprequest: Any | None = ...): ...
def send_file(filepath_or_fp, mimetype: Any | None = ..., as_attachment: bool = ..., filename: Any | None = ..., mtime: Any | None = ..., add_etags: bool = ..., cache_timeout=..., conditional: bool = ...): ...
def content_disposition(filename): ...
def set_safe_image_headers(headers, content): ...
def set_header_field(headers, name, value): ...

root: Any
