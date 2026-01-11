from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Money:
    cents: int

    def __post_init__(self) -> None:
        if self.cents < 0:
            raise ValueError("cents must be >= 0")

    def __repr__(self) -> str:
        return f"Money(cents={self.cents})"

    def __str__(self) -> str:
        dollars = self.cents / 100
        return f"${dollars:,.2f}"

    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented  # type: ignore[return-value]
        return self.cents < other.cents


class Playlist:
    def __init__(self, name: str, songs: list[str]) -> None:
        self.name = name
        self._songs = list(songs)

    def __repr__(self) -> str:
        return f"Playlist(name={self.name!r}, songs={len(self._songs)})"

    def __len__(self) -> int:
        return len(self._songs)

    def __iter__(self) -> Iterator[str]:
        return iter(self._songs)

    def __contains__(self, item: object) -> bool:
        return item in self._songs

    def __getitem__(self, index: int) -> str:
        return self._songs[index]

    def add(self, song: str) -> None:
        self._songs.append(song)


class Timer:
    def __init__(self, label: str = "block") -> None:
        self.label = label
        self._start: float | None = None

    def __enter__(self) -> "Timer":
        import time

        self._start = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> bool:
        import time

        end = time.perf_counter()
        start = self._start or end
        elapsed_ms = (end - start) * 1000
        print(f"{self.label}: {elapsed_ms:.2f} ms")
        return False


def main() -> None:
    wallet = Money(250)
    coffee = Money(425)

    print("repr:", repr(wallet))
    print("str:", wallet)
    print("add:", wallet + coffee)
    print("compare:", wallet < coffee)

    playlist = Playlist("Morning", ["Intro", "Focus", "Break"])
    print("\nplaylist repr:", playlist)
    print("len:", len(playlist))
    print("contains 'Focus':", "Focus" in playlist)
    print("index 1:", playlist[1])

    print("iterate:")
    for song in playlist:
        print("-", song)

    with Timer("loop"):
        total = 0
        for i in range(200_000):
            total += i
    print("total:", total)


if __name__ == "__main__":
    main()
