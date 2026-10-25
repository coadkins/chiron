# chiron

Jupyter Notebook 7, pre-loaded with my preferred extensions and libraries.

- **Editor:** jupyterlab-lsp with the pyrefly language server, ruff formatting
  (jupyterlab-code-formatter), and vim bindings (jupyterlab-vim)
- **Agents:** jupyter-mcp-server, running inside the notebook server at `/mcp`
- **Data:** polars, itables, and altair (plus anywidget for `alt.JupyterChart`)

## Install

```bash
uvx --from git+https://github.com/coadkins/chiron chiron
```

or install it as a tool:

```bash
uv tool install git+https://github.com/coadkins/chiron
chiron
```

`chiron` takes the same options as `jupyter notebook`. It keeps its own Jupyter
config folder (`~/Library/Application Support/chiron/jupyter/config` on macOS),
so it does not touch any other Jupyter install.

## Project kernels

To use a project's dependencies in a notebook, register its `.venv` as a kernel
(the project needs `ipykernel`, e.g. `uv add --dev ipykernel`):

```bash
cd my-project
uvx --from git+https://github.com/coadkins/chiron chiron kernel install
```

The kernel is named after the project folder; use `--name` and `--display-name`
to override, or pass a project path. The kernelspec is written into chiron's own
environment, so it lasts as long as that environment does: with `uv tool
install` that is until you reinstall with `--reinstall`/uninstall, and with a
bare `uvx` run it is only until uv's cache is cleaned.

## Notes

- **One language server at a time.** jupyterlab-lsp uses only the
  highest-priority server for each language. Pyrefly is the default (priority
  60); ruff is registered at priority 40. To use ruff instead, raise its
  priority under Settings → Language Servers.
- **Formatting.** The toolbar's "Format notebook" button runs ruff: first
  `ruff check --fix` to sort imports, then `ruff format`. To format on every
  save, turn on "Auto format config" under Settings → Jupyterlab Code Formatter.
- **Trusted notebooks.** itables tables and altair charts render only in a
  trusted notebook. Notebooks you create are trusted; notebooks from elsewhere
  need the "Not Trusted" button in the top right.
- **MCP:** connect an MCP client to `http://localhost:8888/mcp` (streamable
  HTTP). Adjust the port to match your server, and send the server token.

## Develop

```bash
uv run chiron
```
