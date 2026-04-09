# Average Word Length Is Incorrect, Unrounded, And Sometimes Crashes

`average_word_length()` appears to use the wrong denominator. Text with words
but no sentence punctuation can raise an error instead of returning the average
word length. When it does return a value, it also appears to skip the documented
rounding to two decimal places.

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

Additional example:

```python
from textstats import average_word_length

print(average_word_length("a aa aa."))
```

Expected output:

```text
1.67
```
