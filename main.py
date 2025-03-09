
#### main.py

```python
#!/usr/bin/env python3
import random

realms = [
    "The Obsidian Empire – A land of shadow mages that disappeared in a single night.",
    "The Silver Isles – Floating islands that sank beneath the sea after an unknown catastrophe.",
    "The Moonlit Court – A kingdom where the rulers spoke with the stars, lost when the sky darkened forever.",
    "The Crimson Spire – An advanced civilization reduced to dust after an unknown war.",
    "The Ashen Keep – A fortress that burned for a thousand years before finally vanishing."
]

def get_random_realm():
    return random.choice(realms)

def main():
    print("Welcome to The Vanished Realms!")
    print("Here is a randomly generated lost realm and its fate:")
    print(get_random_realm())

if __name__ == "__main__":
    main()
