# Modulo Three

## How to run the project locally
Please install [UV](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) package manager.

```sh
uv venv --python 3.11
source .venv/bin/activate
uv sync
uv pip install ".[tests]"
```


## Build the project
```sh
uv build
```

# Run unittest with coverage
```sh
uv run pytest
```