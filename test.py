import subprocess

result = subprocess.run(
    ["yay", "-Q"],          # use a list for arguments – no shell needed
    capture_output=True,   # captures both stdout and stderr
    text=True              # decode bytes to str automatically
)

if result.returncode != 0:
    print("Command failed:", result.stderr)
else:
    # `result.stdout` is a single string containing all lines.
    package_list = result.stdout.strip().splitlines()
    print(package_list)   # list of strings, one per line