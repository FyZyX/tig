from typing import Optional

import model.entity


# Lists all available modules in the codebase
def list_modules() -> list[model.entity.Module]:
    pass


def inspect_module(module_path: str) -> model.entity.Module:
    """
    Takes the path to a Python module file (.py) and returns
    a Module object that includes classes, functions,
    and imports from that module.
    """
    pass


def inspect_class(module_path: str, class_name: str) -> model.entity.Class:
    """
    Takes the path to a Python module file and a class name,
    returns a Class object that includes information about
    its methods, fields, and inheritance.
    """
    pass


def inspect_function(
        module_path: str,
        class_name: str | None,
        function_name: str,
) -> model.entity.Function:
    """
    Takes the path to a Python module file, an optional class name,
    and a function name, returns a Function object that includes
    the function signature and source code.
    """
    pass


# Gets a specific module's details
def get_module(module_name: str) -> model.entity.Module:
    pass


# Gets a specific class's details from a module
def get_class(
        module_name: str,
        class_name: str,
) -> model.entity.Class:
    pass


# Gets a specific function's details from a module or class
def get_function(
        module_name: str,
        class_name: Optional[str],
        function_name: str,
) -> model.entity.Function:
    pass


# Adds a new module to the codebase
def add_module(
        module_name: str,
) -> bool:
    pass


# Adds a new class to a module
def add_class(
        module_name: str, class_name: str,
        content: str,
) -> bool:
    pass


# Adds a new function to a module or class
def add_function(
        module_name: str,
        class_name: str | None,
        function_name: str,
        content: str,
) -> bool:
    pass


# Updates an existing function in a module or class
def update_function(
        module_name: str,
        class_name: str | None,
        function_name: str,
        new_content: str,
) -> bool:
    pass
