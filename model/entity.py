from dataclasses import dataclass


@dataclass
class Function:
    name: str
    parameters: list[str]
    return_type: str | None
    code: str


@dataclass
class Class:
    name: str
    functions: list[Function]
    fields: list[str]
    base_classes: list[str]


@dataclass
class Module:
    name: str
    imports: list[str]
    classes: list[Class]
    functions: list[Function]
