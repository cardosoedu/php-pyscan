import subprocess
import shlex
import os

cmds = [
        "egrep --include='*.php' -lr 'eval\/\*'",
        "egrep --include='*.php' -lr '\!?define\('ALREADY_RUN_'",
        "egrep --include='*.php' -lr '\$[A-Za-z]{1,}=Array\(\$[a-z]{1}[0-9A-Za-z]{1,10}\['"
        ]

#work in progress
