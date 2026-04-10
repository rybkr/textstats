# Sentence Count Overcounts Abbreviations And Decimal Points

`sentence_count()` is treating punctuation inside abbreviations and decimals as
full sentence endings. The result is inflated counts for otherwise simple text.

The exact failure mode is a little unclear from the top-level function, but it
looks like sentence splitting was recently moved behind a helper.

## Reproducer

```python
from textstats import sentence_count

print(sentence_count("Dr. Rivera arrived at 3.14 p.m. sharp."))
print(sentence_count("Ms. Chen asked, 'Ready?' Then we left."))
```

Actual output:

```text
5
3
```

Expected output:

```text
1
2
```
