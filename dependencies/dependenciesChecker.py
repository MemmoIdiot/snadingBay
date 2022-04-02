
from json import load
from os import path
from subprocess import call
from typing import Set

from pkg_resources import working_set

with open(path.join('dependencies', 'immigrants.json'), 'r') as f:
    required: Set[str] = set(load(f))

installed: Set[str] = {pkg.key for pkg in working_set}
missing: Set[str] = required - installed
if missing:
    call('python -m pip install'.split(' ')+[*missing, '--user'])
