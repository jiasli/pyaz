# pyaz

A Python wrapper of Azure CLI. Happy scripting with Python!

## Usage

Copy [`pyaz.py`](pyaz.py) to your project and `from pyaz import az`.

## Invocation

Simply call `az("group show --name mygroup")`. The output can be parsed as JSON:

```python
from pyaz import az
import json

accounts = json.loads(az('account list').out)
print("My subscriptions:")
for a in accounts:
    selected = "*" if a["isDefault"] else " "
    print("{} {} {}".format(selected, a["id"], a["name"]))
```

## Return value

The return value of `az()` is a named tuple:

|Field        |Terminal Equivalent
|:-----------:|:-------------------:
|`exit_code`  |`$?`(Bash), `%ERRORLEVEL%`(CMD), `$LastExitCode`(PowerShell)
|`out`        |`stdout`
|`log`        |`stderr`

## Change logging level

To get the same log as `--verbose` or `--debug`, change `pyaz.logging_level` to `logging.INFO` or `logging.DEBUG`.
