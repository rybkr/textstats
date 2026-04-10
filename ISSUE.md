# Summary CLI Ignores `--top-n` And Documents The Wrong Default

The repository now includes a small summary/report path for command-line use,
but it is not honoring the caller's requested top-word count. The CLI help text
also still advertises the old default.

## Reproducer

```python
import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "textstats", "Red blue red green red blue", "--top-n", "2"],
    check=True,
)
```

Actual output:

```text
- red: 3
- blue: 2
- green: 1
```

Expected output:

```text
- red: 3
- blue: 2
```

The `--help` output should also describe the current default top-word count.
