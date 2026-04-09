# Word Count Is Too High With Extra Spaces

When text contains multiple consecutive spaces, `word_count()` reports too many
words because empty chunks are being counted.

## Reproducer

```python
from textstats import word_count

print(word_count("alpha   beta"))
```

Actual output:

```text
4
```

Expected output:

```text
2
```
