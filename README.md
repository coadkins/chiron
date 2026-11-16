# Chiron

JupyterLab, pre-loaded with my preferred extensions, kernels and libraries. This workflow prioritizes quick, ad-hoc investigations, with more progammatic work moving to an IDE. Inspired by [xtralab](https://github.com/jtpio/xtralab).

- **Editor:** [jupyterlab-lsp](https://github.com/jupyter-lsp/jupyterlab-lsp) with the [pyrefly](https://github.com/facebook/pyrefly) language server, [ruff](https://github.com/astral-sh/ruff) and [air](https://github.com/posit-dev/air) for formatting
  ([jupyterlab-code-formatter](https://github.com/jupyterlab-contrib/jupyterlab_code_formatter)), and vim bindings ([jupyterlab-vim](https://github.com/jupyterlab-contrib/jupyterlab-vim)).
- **Kernels:** [ipython](https://github.com/ipython/ipython) for Python and [IRkernel](https://github.com/irkernel/irkernel) for R, both installed with chiron from conda-forge.
- **Agents:** [jupyter-ai](https://github.com/jupyterlab/jupyter-ai), AI code completions and chat.
- **Data:** [polars](https://github.com/pola-rs/polars), [itables](https://github.com/mwouts/itables), [altair](https://github.com/vega/altair) and [anywidget](https://github.com/manzt/anywidget).

Chiron is a [pixi](https://pixi.sh) package built from source with pixi-build, so
R and Python come from the same conda environment.

## Install

### As a global tool

```bash
pixi global install --git https://github.com/coadkins/chiron chiron --expose jupyter
jupyter lab
```

`--expose jupyter` is required: the `chiron` package has no executables of its
own, so without it nothing is put on your PATH. 

To update: `pixi global update chiron`.

### As a project dev dependency

```bash
pixi add --environment dev --git https://github.com/coadkins/chiron chiron
pixi run --environment dev jupyter lab
```

The project's workspace needs `preview = ["pixi-build"]` under `[workspace]`
while pixi-build is a preview feature. Chiron's dependencies are loosely pinned,
but they are solved together with your project's, so conflicting pins are
possible.

## Configuration

Chiron's Jupyter settings (vim bindings, LSP servers, formatters, hidden UI
elements) are installed into the environment's `etc/jupyter` folder, so they
only apply to Jupyter in that environment.

When pixi activates the environment, chiron also sets `JUPYTER_CONFIG_DIR` to
`${XDG_CONFIG_HOME:-~/.config}/chiron/jupyter/config`, so your own lab settings
and workspaces are kept apart from any other Jupyter install.
## R

The R kernel (`ir`) runs the environment's own R from conda-forge. Add R
packages from conda-forge too, e.g. `pixi global add --environment chiron
r-tidyverse` or `pixi add --environment dev r-tidyverse`. `install.packages()`
works, but those packages are not recorded and are lost when the environment is
rebuilt.

## Development

```bash
git clone https://github.com/coadkins/chiron
cd chiron
pixi run lab
```

`pixi run lab` builds chiron from this folder and starts JupyterLab in the
folder you ran it from. After editing files in `jupyter-config/` or `pkg-data/`,
run `pixi install` again so the installed copies are rebuilt.
