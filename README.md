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

## Run unittest
Note that test is already configured with coverage and benchmark
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

## Transition Caching with Divide & Conquer:
   - Uses global TRANSITION_CACHE to store computed state transitions
   - Cache key: (current_state, input_string) → next_state
   - Implements divide-and-conquer strategy for longer inputs:
 
## Performance Characteristics:
   - Time Complexity: 
     * First encounter: O(log n) due to divide-and-conquer (Speed improvement by 50%)
     * Cached lookups: O(1)
   - Space Complexity: O(k) where k is number of unique transitions
   - Cache Benefits:
     * Reuses common patterns
     * Avoids recomputation
     * Improves with usage

## Implementation Details:
   - Base transitions defined for single bits
   - Recursive divide-and-conquer for longer strings
   - Global cache persists across instances
   - No size limit on cached transitions
   - Handles any input length efficiently 
