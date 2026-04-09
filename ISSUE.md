# Average Word Length Is Incorrect And Sometimes Crashes

`average_word_length()` appears to use the wrong denominator. Text with words
but no sentence punctuation can raise an error instead of returning the average
word length.

## Reproducer

```python
from textstats import average_word_length

print(average_word_length("aa bbbb cccccc"))
```

Actual output:

```text
ZeroDivisionError
```

Expected output:

```text
4.0
```
