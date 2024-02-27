import yaml

def yaml_coerce(value):
    # convert value to Python dict
    if isinstance(value, str):
        # yaml.load returns a python object 
        # this function converts string dict to python dict
        # useful beacuse sometimes we need to stringify settings this way (like in a Dockerfile)
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']
    
    return value