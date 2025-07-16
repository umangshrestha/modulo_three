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
   - Uses global TRANSITION_CACHE to store computed state transitions
   - Implements leading zero removal to prevnt unnecesary hit to cache. (Speed improvement by ~10%)

 
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
   - Base transitions defined for single bits
   - Recursive divide-and-conquer for longer strings
   - Global cache persists across instances
   - No size limit on cached transitions
   - Handles any input length efficiently 



# Personal notes
I initially added cache to speed up the long size characters. The iterative approch of O(N) was initally good for small input but left a lot of space for improvements. So, I decided to use dfs with memoization.

Performance got significantly better for medium to large character sets, thanks to our heavy reliance on caching. Even better than for small size characters set.

I tried to minimize maximum cache size to balance memory usage. I did find that limiting the cache to 16 characters strikes a good balance—improving performance across small, medium, and large inputs compared to 8, I assumed the larget the allowed character set the better it can possible get. So I didn’t want to spend time determining the optimal alphabet size to cache. However, since this is a short-running application, the added complexity made the code harder to read and maintain in long term so I decided not to proceed with this alphabet size optimization. So instead I decided to remove leading zeroes to atleast not save long characters that start with 0.