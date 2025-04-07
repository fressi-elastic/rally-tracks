import dataclasses
import importlib
import os
import sys

import pytest


@pytest.fixture
def track():
    track_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if not os.path.isdir(track_dir):
        raise RuntimeError(f"directory not found: {track_dir}")
    path0 = sys.path
    try:
        if track_dir not in path0:
            sys.path = [track_dir] + path0
        return importlib.import_module("track")
    finally:
        sys.path = path0


def test_QueryParamsSource_init(track):
    source = track.QueryParamsSource(DummyTrack(), {})
    assert len(source._queries) == 0


@dataclasses.dataclass()
class DummyIndex:
    name: str = "dummy"


@dataclasses.dataclass()
class DummyTrack:
    indices: tuple[DummyIndex, ...] = (DummyIndex(),)

    def index_names(self) -> list[str]:
        return [i.name for i in self.indices]
