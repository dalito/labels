# -*- coding: utf-8 -*-
"""
Convert old style gitea label file (gitea <1.19.0) to toml format
https://docs.gitea.io/en-us/customizing-gitea/#labels
"""

import sys
from pathlib import Path

import tomli_w


def convert(fpath: Path) -> None:
    print(f"loading {fpath.resolve()}")
    with open(fpath, mode="rt") as fp:
        txtlabels = fp.readlines()

    toml_labels = {}
    for line in txtlabels:
        if not line.strip():
            continue
        color, tmp = line.split(" ", maxsplit=1)
        name, description = tmp.split(";", maxsplit=1)
        toml_labels[f"{name.strip()}"] = {
            "color": f"{color.strip('#')}",
            "description": f"{description.strip()}",
            "name": f"{name.strip()}",
        }

    outfn = fpath.with_suffix(".toml")
    with open(outfn, mode="wb") as fp:
        tomli_w.dump(toml_labels, fp)

    print(f"--> {outfn.resolve()}")


if __name__ == "__main__":
    convert(Path(sys.argv[1]))
