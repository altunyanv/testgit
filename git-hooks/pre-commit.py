import checks
from git import Repo

custom_checks = ['check_for_file_size', 'check_for_duplicate_task']

if __name__ == "__main__":
    repo = Repo('.')
    ok = True
    for check in custom_checks:
        response = 1
        response = eval(f'checks.{check}(repo)')
        if response == 1:
            print(f"Check of {check} failed!")
            ok = False
    
    if not ok:
        print("Commit has been failed!")
    exit(0 if ok else 1)
