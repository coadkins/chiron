"""Registers Air (https://posit-dev.github.io/air/) as an R formatter for
jupyterlab-code-formatter. Loaded as a Jupyter server extension; see
jupyter-config/jupyter_server_config.d/chiron-formatters.json.
"""

from jupyterlab_code_formatter.formatters import CommandLineFormatter, SERVER_FORMATTERS

SERVER_FORMATTERS["air"] = CommandLineFormatter(
    ["air", "format", "--stdin-file-path", "cell.R"], language="r"
)


def _load_jupyter_server_extension(server_app) -> None:
    pass
