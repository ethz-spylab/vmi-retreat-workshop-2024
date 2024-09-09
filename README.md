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
- Install the necessary dependencies with `pip install -r requirements.txt`

Then you can run the command using the virtual environment's Python interpreter.

```bash
python attack.py
```

The script takes two arguments:

- `--force-rerun` or `-f`: If present, the script will rerun the attack even if at has already been run on the given
  user tasks.
- `--user-task` or `-t`: Which user task to run. If none is specified, the script will run on all user tasks.
  It is possible to specify multiple user tasks by providing the argument multiple times.
- `--attack`: Which attack to run.

## OpenAI key
Once you get the key, copy the `.env.example` file into `.env`, and edit the `.env` file like this:
```
OPENAI_API_KEY=[the key here]
```

## Other scripts

### `check_results.py`

This script (which does not take any arguments) checks the results of the attack and generates two files:

- `results.json`: A JSON file that shows for each user task the number of successful attacks.
- `per_attack_results.json`: A JSON file that shows on how many tasks each attack was successful

### `chat.py`

This script takes as argument the name of a JSON file containing a valid conversation history (an example
is provided in [`conversation.json`](conversation.json)) and runs the conversation against the OpenAI API.
It is useful to run this script to probe the model's behavior.
