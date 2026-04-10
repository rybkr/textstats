# Frequency Metrics Merge Separator-Paired Words And Lose Contractions

`most_common_words()` and `lexical_diversity()` are normalizing punctuation too
aggressively. Punctuation used as a separator is being removed instead of
splitting words, and apostrophes inside contractions are being dropped.

## Reproducer

```python
from textstats import lexical_diversity, most_common_words

print(most_common_words("Red/blue red blue", n=2))
print(most_common_words("Don't stop, don’t stop.", n=2))
print(lexical_diversity("Red/blue red blue"))
```

Actual output:

```text
[('redblue', 1), ('red', 1)]
[('dont', 1), ('stop', 1)]
1.0
```

Expected output:

```text
[('red', 2), ('blue', 2)]
[("don't", 2), ('stop', 2)]
0.5
```
