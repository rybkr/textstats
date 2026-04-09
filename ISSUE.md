# Most Common Words Treat Punctuation Variants As Different Words

`most_common_words()` is counting punctuation-attached tokens separately, so
`"hello"` and `"hello,"` do not get merged into the same word count.

## Reproducer

```python
from textstats import most_common_words

print(most_common_words("Hello, hello! HELLO? Bye.", n=2))
```

Actual output:

```text
[('hello,', 1), ('hello!', 1)]
```

Expected output:

```text
[('hello', 3), ('bye', 1)]
```
