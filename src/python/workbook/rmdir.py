from os import walk, remove, rmdir as _rmdir, path as osp

def rmdir(root:str):
    traverse = walk(root)
    stack = []
    for (dpath, dnames, fnames) in traverse:
        stack.append(dpath)
        for fname in fnames:
            remove(osp.join(dpath,fname))

    while stack:
        _rmdir(stack.pop())



