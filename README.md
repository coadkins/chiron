# Chiron

JupyterLab, pre-loaded with my preferred extensions and libraries. This workflow prioritizes quick, ad-hoc investigations, with more progammatic work moving to an IDE. Inspired by [xtralab](https://github.com/jtpio/xtralab).

- **Editor:** [jupyterlab-lsp](https://github.com/jupyter-lsp/jupyterlab-lsp) with the [pyrefly](https://github.com/facebook/pyrefly) language server, [ruff](https://github.com/astral-sh/ruff) and [air](https://github.com/posit-dev/air) for formatting.  
**Kernels**: [ipython](https://github.com/ipython/ipython) for Python, [ggsql-jupyter](https://github.com/posit-dev/ggsql/tree/main/ggsql-jupyter) for DuckDB / SQL. [IRkernel](https://github.com/irkernel/irkernel) is installed seperately, outside of the tool environment.
  ([jupyterlab-code-formatter](https://github.com/jupyterlab-contrib/jupyterlab_code_formatter)), and vim bindings ([jupyterlab-vim](https://github.com/jupyterlab-contrib/jupyterlab-vim))
- **Agents:** [jupyter-ai-lite](https://github.com/jupyterlab/jupyter-ai-lite), AI code completions and chat running entirely in the browser. 
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

`chiron` takes the same options as `jupyter lab`. It keeps its own Jupyter
config folder, so it does not touch any other Jupyter install.

## SQL kernel

`ggsql-jupyter` is installed with chiron. On launch, `chiron` checks for a
`ggsql` kernelspec and registers one in its own environment if it is missing,
so like the project kernels it lasts as long as that environment does.
Confirm with `jupyter kernelspec list`.

## Python project kernels

To use a project's dependencies in a notebook, register its `.venv` as a kernel
(the project needs `ipykernel`):

```bash
cd my-project
uvx --from git+https://github.com/coadkins/chiron chiron kernel install
```

The kernel is named after the project folder; use `--name` and `--display-name`
to override, or pass a project path. The kernelspec is written into chiron's own
environment, so it lasts as long as that environment does.

## R kernel

To use the `IRkernel` package, install it in your system's default R library and register the kernel using chiron: 

```bash
chiron kernel install-r
```
This runs `IRkernel::installspec()` with chiron's version of `jupyter` on PATH and writes
the kernelspec into chiron's own environment (`--sys-prefix`), so other Jupyter
installs do not see it, and it lasts as long as that environment does.
