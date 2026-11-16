# Installed to $PREFIX/etc/conda/activate.d/ and run when pixi activates the
# environment. Gives chiron its own Jupyter config folder (user settings,
# workspaces), apart from any other Jupyter install. This is the same folder
# the old `chiron` command used on Linux.
export JUPYTER_CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/chiron/jupyter/config"
