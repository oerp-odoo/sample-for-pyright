from collections import defaultdict
from collections.abc import Mapping
from typing import Any
from weakref import WeakSet

from .modules.registry import Registry
from .sql_db import Cursor
from .tools import StackMap

__all__: Any
_logger: Any
INHERITED_ATTRS: Any

class Params:
    args: Any
    kwargs: Any
    def __init__(self, args, kwargs) -> None: ...
    def __str__(self): ...

class Meta(type):
    def __new__(meta, name, bases, attrs): ...

def attrsetter(attr, value): ...
def propagate(method1, method2): ...
def constrains(*args): ...
def ondelete(at_uninstall): ...
def onchange(*args): ...
def depends(*args): ...
def depends_context(*args): ...
def returns(model, downgrade: Any | None = ..., upgrade: Any | None = ...): ...
def downgrade(method, value, self, args, kwargs): ...
def split_context(method, args, kwargs): ...
def autovacuum(method): ...
def model(method): ...

_create_logger: Any

def _model_create_single(create, self, arg): ...
def model_create_single(method): ...
def _model_create_multi(create, self, arg): ...
def model_create_multi(method): ...
def _call_kw_model(method, self, args, kwargs): ...
def _call_kw_model_create(method, self, args, kwargs): ...
def _call_kw_multi(method, self, args, kwargs): ...
def call_kw(model, name, args, kwargs): ...

class Environment(Mapping):
    _local: Any = ...
    cr: Cursor = ...
    uid: int = ...
    context: dict = ...
    envs: Any
    @classmethod
    def manage(cls) -> None: ...
    def reset(self) -> None: ...
    transaction: Transaction
    registry: Registry
    cache: Cache
    _cache_key: Any
    _protected: Any
    def __new__(cls, cr: Cursor, uid, context, su: bool = ...) -> Environment: ...
    def __contains__(self, model_name): ...
    def __getitem__(self, model_name): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(self, cr: Cursor | None = ..., user: Any | None = ..., context: Any | None = ..., su: Any | None = ...) -> Environment: ...
    def ref(self, xml_id, raise_if_not_found: bool = ...): ...
    def is_superuser(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_system(self) -> bool: ...
    @property
    def user(self):
        return self['res.users']
    @property
    def company(self):
        return self['res.company']
    @property
    def companies(self):
        return self['res.company']
    @property
    def lang(self) -> str: ...
    def clear(self) -> None: ...
    def clear_upon_failure(self): ...
    def is_protected(self, field, record): ...
    def protected(self, field): ...
    def protecting(self, what, records: Any | None = ...) -> None: ...
    def fields_to_compute(self): ...
    def records_to_compute(self, field): ...
    def is_to_compute(self, field, record): ...
    def not_to_compute(self, field, records): ...
    def add_to_compute(self, field, records): ...
    def remove_to_compute(self, field, records) -> None: ...
    def norecompute(self) -> None: ...
    def cache_key(self, field): ...

class Transaction:
    registry: Any
    envs: WeakSet
    cache: Cache
    protected: StackMap
    tocompute: defaultdict
    towrite: defaultdict
    def __init__(self, registry): ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def reset(self) -> None: ...

NOTHING: Any
EMPTY_DICT: Any

class Cache:
    _data: Any
    def __init__(self) -> None: ...
    def _get_field_cache(self, model, field): ...
    def _set_field_cache(self, model, field): ...
    def contains(self, record, field): ...
    def get(self, record, field, default=...): ...
    def set(self, record, field, value) -> None: ...
    def update(self, records, field, values) -> None: ...
    def remove(self, record, field) -> None: ...
    def get_values(self, records, field) -> None: ...
    def get_until_miss(self, records, field): ...
    def get_records_different_from(self, records, field, value): ...
    def get_fields(self, record) -> None: ...
    def get_records(self, model, field): ...
    def get_missing_ids(self, records, field) -> None: ...
    def invalidate(self, spec: Any | None = ...) -> None: ...
    def check(self, env) -> None: ...