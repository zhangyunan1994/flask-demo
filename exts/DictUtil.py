def remove_none_key(param: dict):
    for k in list(param.keys()):
        if not param[k]:
            del param[k]
