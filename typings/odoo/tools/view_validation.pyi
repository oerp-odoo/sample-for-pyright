from typing import Any

_logger: Any
_validators: Any
_relaxng_cache: Any
READONLY: Any

def _get_attrs_symbols(): ...
def get_variable_names(expr): ...
def get_dict_asts(expr): ...
def _check(condition, explanation) -> None: ...
def get_domain_identifiers(expr): ...
def valid_view(arch, **kwargs): ...
def validate(*view_types): ...
def relaxng(view_type): ...
def schema_valid(arch, **kwargs): ...
