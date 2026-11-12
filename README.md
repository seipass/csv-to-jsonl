# csv-to-jsonl

CSV to JSON records converter.

## Usage

Install with `pip install .`. Pipe input into `csv-to-jsonl` or pass a file path. Structured JSON tools accept JSON on stdin; CSV tools accept CSV; text and URL tools accept plain text. Output is written to stdout.

```sh
printf '%s' '{"sample": 1}' | csv-to-jsonl
python -m pytest
```

## Development

Python 3.9+. Run tests with `python -m pytest`. MIT licensed.
