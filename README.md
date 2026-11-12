# tiny-chess-01

A compact chess engine in 4,096 bytes of Python. Alpha-beta search with
quiescence, MVV-LVA move ordering, and a fixed 100,000-node budget per move.
Material-only evaluation. Deterministic: no clock, no randomness.

Run: `MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py`
