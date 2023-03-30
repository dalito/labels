# -*- coding: utf-8 -*-
"""
Convert toml file to "advanced gitea label format" (requires gitea >=1.19.0)
https://docs.gitea.io/en-us/customizing-gitea/#labels
"""

import sys
from pathlib import Path

import tomli
import yaml

# We produce output with ordered keys that exactly matches the example file
# of gitea.  This may not be required (not tested).
gitea_key_order = ["name", "color", "description"]


def convert(fpath: Path) -> None:
    print(f"loading {fpath.resolve()}")
    with open(fpath, mode="rb") as fp:
        labels = tomli.load(fp)

    gitea_labels = []
    for label in labels.values():
        gitea_labels.append({k: label[k] for k in gitea_key_order})

    outfn = fpath.with_suffix(".yaml")
    with open(outfn, mode="wt", encoding="utf-8") as fp:
        yaml.safe_dump({"labels": gitea_labels}, fp, sort_keys=False)

    print(f"--> {outfn.resolve()}")


if __name__ == "__main__":
    convert(Path(sys.argv[1]))
