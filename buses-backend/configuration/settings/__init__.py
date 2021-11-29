from .base import *

if ENVIRONMENT == ENV_DEVELOPMENT:
    from .local import *
else:
    from .docker import *
