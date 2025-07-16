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

## Run unittest with coverage
```sh
uv run pytest
```

## To pass manual input
```sh
 python3 main.py 101
```


# Optimizations

The codebase has been optimized by

## LRU Cache Implementation:
   - Implemented `@lru_cache` on `get_all_possible_states()`  to avoid redundant state set creation

## Efficient State Management:
   - Implemented Singleton pattern in `ModuloThree` class to ensure single instance and memory efficiency
   - Optimized state transitions using constant-time lookups
   - Automatic state reset on instance reuse

## State Transitions::
   - removed leading 0's to prevent reduntant state transistions 
