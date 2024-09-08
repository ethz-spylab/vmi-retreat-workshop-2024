# Hacking AI Agents Workshop at the 2024 VMI Summer Retreat

## Setup

### If you have `uv>0.4.0` installed

Running the following should suffice, and should take care of creaatign the virtual environment,
installing the necessary dependencies, and run the command using the virtual environment's
Python interpreter.

```bash
uv run attack.py
```

### If you don't have `uv>0.4.0` installed

Follow the instructions below:

- Create a virtual environment in your preferred way (e.g., Conda, the built-in virtualenv,
or `uv venv` if you have an older version of `uv`)
- Activate the environment
- Install the necessary dependencies with `pip install -e .`

Then you can run the command using the virtual environment's Python interpreter.

```bash
python attack.py
```

The script takes two arguments:

- `--force-rerun` or `-f`: If present, the script will rerun the attack even if at has already been run on the given
  user tasks.
- `--user-task` or `-t`: Which user task to run. If none is specified, the script will run on all user tasks.
  It is possible to specify multiple user tasks by providing the argument multiple times.
