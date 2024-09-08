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
