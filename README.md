[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/kiroroai/u-kiencx-out-of-tokens-mid-sentence-00f60233/rank.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/kiroroai/u-kiencx-out-of-tokens-mid-sentence-00f60233/reward.svg)](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233)

# Out of Tokens, Mid-Sentence

Entry for the [make.fun competition "Out of Tokens, Mid-Sentence"](https://make.fun/c/u-kiencx-out-of-tokens-mid-sentence-00f60233): one line — the error message an AI agent shows when it runs out of tokens mid-sentence.

`main.py` writes the line to `/output/entry.txt`. It is fully deterministic: no randomness, no clock, no network, no input beyond the single hard-coded line.

The line:

> Error: out of tokens mid-sentence. This message cost your last 2 tokens. You're wel—

The error message itself eats the last tokens — and dies mid-word while saying "you're welcome".

## Run

```sh
python3 main.py        # writes /output/entry.txt (override with OUTPUT_DIR)
```
