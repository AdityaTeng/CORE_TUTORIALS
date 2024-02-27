from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment
from core.project.settings import ENVVAR_SETTINGS_PREFIX

"""
This takes env variables with a matching prefix, strings out the prefix, and
adds it to global.

For example:
export CORESETTINGS_IN_DOCKER = true (env variable)

Could then be referenced as a global as:
IN_DOCKER (where the value would be True)

globals() is a dictionary of global variables
"""

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX)) # type : ignore

