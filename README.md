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
Note that the test is already configured with coverage and benchmark
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
   - Implemented Singleton pattern in `ModuloThree` class to ensure a single instance and memory efficiency
   - Optimized state transitions using constant-time lookups
   - Automatic state reset on instance reuse
   - Uses global TRANSITION_CACHE to store computed state transitions
   - Implements leading zero removal to prevent unnecessary hits to the cache. (Cache improvement by ~10%)

 
## Performance Characteristics:
   - Time Complexity: 
     * First encounter: O(log n) due to divide-and-conquer (Speed improvement by ~50%)
     * Cached lookups: O(1)
   - Space Complexity: O(k) where k is number of unique transitions
   - Cache Benefits:
     * Reuses common patterns
     * Avoids recomputation
     * Improves with usage

## Implementation Details:
   - Base transitions are defined for single bits
   - Recursive divide-and-conquer for longer strings
   - Global cache persists across instances
   - No size limit on cached transitions
   - Handles any input length efficiently 



# Personal notes
I initially added caching to speed up the processing of long, character-filled strings. The iterative approach of O(N) was initially suitable for small inputs, but left considerable room for improvement. So, I decided to use DFS with memoization.

Performance got significantly better for medium to large character sets, thanks to our heavy reliance on caching. Even better than for a small character set.

I tried to minimize the maximum cache size to balance memory usage. I found that limiting the cache to 16 characters strikes a good balance, improving performance across small, medium, and large inputs compared to 8. I assumed the larger the allowed character set, the better it can get. So I didn’t want to spend time determining the optimal alphabet size to cache. However, since this is a short-running application, the added complexity made the code harder to read and maintain in the long term. The performance gain didn't justify the added complexity, so I decided not to proceed with this alphabet size optimization. Instead, I decided to remove leading zeroes to avoid saving long characters that start with 0, which yielded a modest gain.
