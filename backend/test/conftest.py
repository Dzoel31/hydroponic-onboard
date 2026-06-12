import importlib
import os
import sys
from pathlib import Path

from fastapi import FastAPI


BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))


os.environ.setdefault("PGHOST", "localhost")
os.environ.setdefault("PGPORT", "5432")
os.environ.setdefault("PGDATABASE", "hydroponic_test")
os.environ.setdefault("PGUSER", "postgres")
os.environ.setdefault("PGPASSWORD", "postgres")


def import_fresh(module_name: str):
    if module_name in sys.modules:
        del sys.modules[module_name]
    return importlib.import_module(module_name)


def get_fastapi_app() -> FastAPI:
    main = import_fresh("main")

    assert hasattr(main, "app"), (
        "main.py harus memiliki variable bernama `app`. "
        "Clue: buat `app = FastAPI()` di main.py."
    )

    assert isinstance(main.app, FastAPI), (
        "`app` di main.py harus berupa instance FastAPI. "
        "Clue: import FastAPI dari fastapi, lalu buat app dari class itu."
    )

    return main.app
