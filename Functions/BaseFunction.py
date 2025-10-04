def base_function(func, **kwargs):
    try:
        return func(**kwargs)
    except Exception as e:
        raise Exception(str(e))
