"""The `chiron` command: JupyterLab with chiron's configuration folder."""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import platformdirs


def config_dir() -> str:
    """The Jupyter config folder of chiron, kept apart from other Jupyter installs."""
    root = platformdirs.user_config_dir("chiron", appauthor=False, roaming=True)
    return os.path.join(root, "jupyter", "config")


def venv_python(project: Path) -> Path:
    """The interpreter of the project's .venv."""
    sub = "Scripts/python.exe" if os.name == "nt" else "bin/python"
    # Deliberately not resolved: a venv's python symlinks to the base
    # interpreter, which would lose the venv's site-packages.
    return project / ".venv" / sub


def kernel_install(argv: list[str]) -> int:
    """Register a project's .venv as a kernel in chiron's environment."""
    parser = argparse.ArgumentParser(
        prog="chiron kernel install",
        description="Register a project's .venv as a Jupyter kernel.",
    )
    parser.add_argument(
        "project", nargs="?", default=".", help="project folder (default: .)"
    )
    parser.add_argument("--name", help="kernel name (default: the project folder name)")
    parser.add_argument(
        "--display-name", help="name shown in Jupyter (default: Python (<name>))"
    )
    args = parser.parse_args(argv)

    project = Path(args.project).expanduser().absolute()
    python = venv_python(project)
    if not python.exists():
        print(f"chiron: no virtualenv at {project / '.venv'} (try `uv sync`)", file=sys.stderr)
        return 1

    check = subprocess.run(
        [str(python), "-c", "import ipykernel"], capture_output=True, text=True
    )
    if check.returncode != 0:
        print(
            f"chiron: ipykernel is not installed in {project / '.venv'}; "
            "add it with `uv add --dev ipykernel`",
            file=sys.stderr,
        )
        return 1

    name = re.sub(r"[^a-z0-9._-]+", "-", (args.name or project.name).lower()).strip("-")
    if not name:
        print("chiron: could not derive a kernel name; pass --name", file=sys.stderr)
        return 1
    spec = {
        "argv": [str(python), "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": args.display_name or f"Python ({args.name or project.name})",
        "language": "python",
        "metadata": {"debugger": True},
    }

    from jupyter_client.kernelspec import KernelSpecManager

    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "kernel.json").write_text(json.dumps(spec, indent=1))
        dest = KernelSpecManager().install_kernel_spec(
            tmp, kernel_name=name, prefix=sys.prefix
        )
    print(f"Installed kernel '{name}' ({spec['display_name']}) to {dest}")
    return 0


def ensure_ggsql_kernel() -> None:
    """Register the ggsql kernel in chiron's environment unless it is already known."""
    from jupyter_client.kernelspec import KernelSpecManager

    if "ggsql" in KernelSpecManager().find_kernel_specs():
        return
    bindir = Path(sys.executable).parent
    exe = bindir / ("ggsql-jupyter.exe" if os.name == "nt" else "ggsql-jupyter")
    if not exe.exists():
        return
    # ggsql-jupyter shells out to `jupyter`, which may not be on PATH (uvx).
    env = {**os.environ, "PATH": os.pathsep.join([str(bindir), os.environ.get("PATH", "")])}
    result = subprocess.run(
        [str(exe), "--install", "--sys-prefix"], env=env, capture_output=True, text=True
    )
    if result.returncode == 0:
        print("chiron: registered the ggsql kernel", file=sys.stderr)
    else:
        print(
            f"chiron: could not register the ggsql kernel: {result.stderr.strip()}",
            file=sys.stderr,
        )


def main() -> None:
    """Run `jupyter lab` with chiron's config folder."""
    if sys.argv[1:3] == ["kernel", "install"]:
        sys.exit(kernel_install(sys.argv[3:]))
    # Jupyter reads JUPYTER_CONFIG_DIR at import time, so set it before
    # importing jupyterlab.
    os.environ.setdefault("JUPYTER_CONFIG_DIR", config_dir())
    ensure_ggsql_kernel()
    from jupyterlab.labapp import main as lab_main

    lab_main()
