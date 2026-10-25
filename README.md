# chiron

Jupyter Notebook 7, pre-loaded with my preferred extensions and libraries. This workflow prioritizes quick, ad-hoc investigations, with more progammatic work moving to an IDE. Inspired by [xtralab](https://github.com/jtpio/xtralab).

- **Editor:** [jupyterlab-lsp](https://github.com/jupyter-lsp/jupyterlab-lsp) with the [pyrefly](https://github.com/facebook/pyrefly) language server, [ruff](https://github.com/astral-sh/ruff) formatting
  ([jupyterlab-code-formatter](https://github.com/jupyterlab-contrib/jupyterlab_code_formatter)), and vim bindings ([jupyterlab-vim](https://github.com/jupyterlab-contrib/jupyterlab-vim))
- **Agents:** [jupyter-server-mcp](https://github.com/jupyter-ai-contrib/jupyter-server-mcp) exposing [jupyter-ai-tools](https://github.com/jupyter-ai-contrib/jupyter-ai-tools) notebook tools and JupyterLab commands, running inside the notebook server
- **Data:** [polars](https://github.com/pola-rs/polars), [itables](https://github.com/mwouts/itables), [altair](https://github.com/vega/altair) and [anywidget](https://github.com/manzt/anywidget).

## Install

```bash
uvx --from git+https://github.com/coadkins/chiron chiron
```

or install it as a persistent tool:

```bash
uv tool install git+https://github.com/coadkins/chiron
chiron
```

`chiron` takes the same options as `jupyter notebook`. It keeps its own Jupyter
config folder, so it does not touch any other Jupyter install.

## Project kernels

To use a project's dependencies in a notebook, register its `.venv` as a kernel
(the project needs `ipykernel`):

```bash
cd my-project
uvx --from git+https://github.com/coadkins/chiron chiron kernel install
```

The kernel is named after the project folder; use `--name` and `--display-name`
to override, or pass a project path. The kernelspec is written into chiron's own
environment, so it lasts as long as that environment does: with `uv tool
install` that is until you reinstall with `--reinstall`/uninstall, and with a
bare `uvx` run it is only until uv's cache is cleaned.
