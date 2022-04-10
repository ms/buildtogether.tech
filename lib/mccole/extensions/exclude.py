"""Exclude files."""

from pathlib import Path
import ivy

@ivy.filters.register(ivy.filters.Filter.LOAD_NODE_DIR)
def filter_dirs(value, filepath):
    """Exclude directories that contain `.ivyignore`."""
    ignore = filepath.parent.joinpath(".ivyignore")
    if not ignore.exists():
        return True
    with open(ignore, "r") as reader:
        excludes = set([x.strip() for x in reader.readlines()])
        return filepath.name not in excludes
