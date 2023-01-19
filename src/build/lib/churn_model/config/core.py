from pathlib import Path
from strictyaml import load, YAML
import typing as t
from pydantic import BaseModel

PACKAGE_DIR = Path(__file__).resolve().parent.parent
ROOT = PACKAGE_DIR.parent
CONFIG_FILE_PATH = PACKAGE_DIR / 'config.yaml'
BEST_MODEL_DIR = PACKAGE_DIR / 'models'
DATA_DIR = PACKAGE_DIR / 'data/raw'


class AppConfig(BaseModel):

    package_name: str

    x_train: str
    y_train: str
    x_test: str
    y_test: str

    saved_model_name: str
    saved_pipeline_name: str
    final_pipeline: str


class ModelConfig(BaseModel):

    categorical: t.Sequence[str]
    drop: t.Sequence[str]
    nullFillMode: t.Sequence[str]
    nullFillZero: t.Sequence[str]
    numerical: t.Sequence[str]
    rename: t.Dict
    features: t.Sequence[str]


class Config(BaseModel):

    app_config: AppConfig
    model_config: ModelConfig


def find_config_path() -> Path:
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f'config not in {CONFIG_FILE_PATH}')


def fetch_config_file(cfg_path: Path = None) -> YAML:

    if not cfg_path:
        cfg_path = find_config_path()

    with open(cfg_path, 'r') as f:
        parsed_config = load(f.read())
        return parsed_config

    raise OSError(f'didnot find config file at {cfg_path}')


def create_and_validate_config(parsed_config: YAML = None) -> Config:

    if parsed_config is None:
        parsed_config = fetch_config_file()

    _config = Config(app_config=AppConfig(**parsed_config.data),
                     model_config=ModelConfig(**parsed_config.data))

    return _config


config = create_and_validate_config()
