# Tiny Chess Engine (tiny-chess-01 entry)

A fully functional competitive chess engine entry for the [make.fun](https://make.fun) `tiny-chess-01` challenge, packed into strictly under 4,096 bytes of Python code.

## What It Is

This repository contains a high-performance, ultra-compact chess engine implemented in pure Python (standard library only). Despite the strict 4,096-byte size limit on `main.py`, the engine features sophisticated search and evaluation algorithms to compete effectively in automated tournaments.

## How It Works

- **Platform**: Written for Python 3.13, utilizing zero external dependencies.
- **Search Algorithm**: Implements negamax alpha-beta pruning with quiescence search to avoid the horizon effect on tactical captures.
- **Move Ordering**: Uses Most Valuable Victim / Least Valuable Aggressor (MVV-LVA) heuristic to optimize alpha-beta pruning efficiency.
- **Evaluation**: Incorporates material counting combined with a pawn Piece-Square Table (PST) for positional awareness.
- **Node Budget**: Bounded search utilizing a 100,000 node budget per turn, ensuring deterministic play and strict adherence to game time limits without relying on wall-clock time.

## How to Run & Grade

The engine plays via the `make.fun` environment HTTP API. To test and grade locally using Docker and the `make.fun` CLI:

```bash
makefun grade-local --kit . --bot <your repository> --driver docker
```

To run pre-submit validation checks (including size caps):

```bash
makefun check
```

## License

MIT License. See [LICENSE](LICENSE) for details.
