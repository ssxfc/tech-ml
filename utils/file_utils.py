import os
import pathlib


def touch_dir(fp: str):
    """
    create a new dir
    """
    path_obj = pathlib.Path(fp)
    # 如果不存在就新建
    if not path_obj.exists():
        path_obj.mkdir(mode=755)


def rm_tree(fp):
    """
    recurrently removal of directory
    """
    pth = pathlib.Path(fp)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()