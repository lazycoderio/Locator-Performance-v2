import yaml

class Config(object):
    def __init__(self):
        with open("env_vars.yaml", "r") as f:
            self.env_vars = yaml.load(f, Loader=yaml.FullLoader)