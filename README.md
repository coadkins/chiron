# chiron

Jupyter Notebook 7, pre-loaded with my preferred extensions and libraries.

- **Editor:** jupyterlab-lsp with the pyrefly language server, ruff formatting
  (jupyterlab-code-formatter), and vim bindings (jupyterlab-vim)
- **Agents:** jupyter-mcp-server, running inside the notebook server at `/mcp`
- **Data:** polars, itables, and altair (plus anywidget for `alt.JupyterChart`)

## Install

```bash
uvx --from git+https://github.com/<you>/chiron chiron
```

or install it as a tool:

```bash
uv tool install git+https://github.com/<you>/chiron
chiron
```

`chiron` takes the same options as `jupyter notebook`. It keeps its own Jupyter
config folder (`~/Library/Application Support/chiron/jupyter/config` on macOS),
so it does not touch any other Jupyter install.

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
