"""The `chiron` command: Jupyter Notebook with chiron's configuration folder."""

import os

import platformdirs


def config_dir() -> str:
    """The Jupyter config folder of chiron, kept apart from other Jupyter installs."""
    root = platformdirs.user_config_dir("chiron", appauthor=False, roaming=True)
    return os.path.join(root, "jupyter", "config")


def main() -> None:
    """Run `jupyter notebook` with chiron's config folder."""
    # Jupyter reads JUPYTER_CONFIG_DIR at import time, so set it before
    # importing notebook.
    os.environ.setdefault("JUPYTER_CONFIG_DIR", config_dir())
    from notebook.app import main as notebook_main

    notebook_main()
