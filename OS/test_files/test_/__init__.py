def prog_tiles():
    import importlib
    from test_.prog1 import title as prog1title
    prog2 = importlib.import_module("test_.prog 2")
    prog_titles = [prog1title(), prog2.title()]
    return prog_titles