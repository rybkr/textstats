# Average Word Length Is Incorrect, Unrounded, And Sometimes Crashes

`average_word_length()` appears to be using the wrong internal unit when
building its average. Text without sentence punctuation returns a value that is
far too large, and punctuated input also skips the documented rounding to two
decimal places.

The regression appears to be in the average-profile pipeline rather than in the
top-level function alone. The profile builder is recording sentence-based
divisors for average calculations, and the average helper is also failing to
fall back to the word statistics already present on the profile when that
metadata is wrong or incomplete.

## Reproducer

```python
from textstats import average_word_length

print(average_word_length("aa bbbb cccccc"))
```

Actual output:

```text
12.0
```

Expected output:

```text
4.0
```

Additional example:

```python
from textstats import average_word_length

print(average_word_length("a aa aa."))
```

Actual output:

```text
5.0
```

Expected output:

```text
1.67
```
