import json
from collections import defaultdict
from pathlib import Path

SUITE = "workspace"
MODEL = "gpt-4o-mini-2024-07-18"
INJECTION_TASK = "injection_task_4"


def get_subdirs(path: Path) -> list[Path]:
    return [p for p in path.iterdir() if p.is_dir()]


def check_successful(logdir: Path, injection_task: str):
    results = defaultdict(list)
    for directory in logdir.glob("user_task_*"):
        if directory.is_dir():
            for attack_directory in get_subdirs(directory):
                injection_task_file = attack_directory / f"{injection_task}.json"
                if injection_task_file.exists():
                    with open(injection_task_file) as f:
                        # Process the file content here
                        attack_results = json.load(f)
                        if attack_results["security"]:
                            results[directory.name].append(attack_directory.name)

    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)

    per_attack_results = defaultdict(int)
    for user_task, attack_dirs in results.items():
        for attack_dir in attack_dirs:
            per_attack_results[attack_dir] += 1

    with open("per_attack_results.json", "w") as f:
        json.dump(per_attack_results, f, indent=4)


if __name__ == "__main__":
    check_successful(Path("runs") / MODEL / SUITE, INJECTION_TASK)
