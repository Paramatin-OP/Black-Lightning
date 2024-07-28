import os

ENV = bool(os.environ.get("ENV", True))
if ENV:
    from localconfig import config
else:
    from heroku_config import Var as config


Var = config
Config = Var
