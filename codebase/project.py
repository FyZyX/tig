import fnmatch
import pathlib
import typing

import config
from . import file


class Project:
    def __init__(self, path: pathlib.Path):
        self._path = path

        self._excludes = config.DEFAULT_EXCLUDES
        self._update_exclusion_patterns()

    def _update_exclusion_patterns(self):
        gitignore_path = self._path / ".gitignore"
        if not gitignore_path.is_file():
            return
        ignored = file.parse_gitignore(gitignore_path)
        self._excludes.extend(ignored)

    def _should_exclude(self, entry: pathlib.Path) -> bool:
        return any(
            fnmatch.fnmatch(entry.name, pattern)
            for pattern in self._excludes
        )

    def _iter_path(self, path: pathlib.Path) -> typing.Iterable[pathlib.Path]:
        for entry in sorted(path.iterdir(), key=lambda e: e.name):
            if self._should_exclude(entry):
                continue
            yield entry

    def structure(
            self,
            path: pathlib.Path = None,
            indent: str = "",
            depth: int | None = None,
    ):
        path = path or self._path

        if depth is not None:
            if depth <= 0:
                return
            depth -= 1

        for entry in self._iter_path(path):
            print(f"{indent}{entry.name}")
            if entry.is_dir():
                self.structure(entry, indent + "\t", depth)
