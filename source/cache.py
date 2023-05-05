class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        assert capacity >= 1
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ''
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            lru_key = next(iter(self.cache))
            del self.cache[lru_key]

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
