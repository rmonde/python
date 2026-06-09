# Python Learning — Claude Working Notes

## How we work
- Rahul writes code, Claude reviews and gives feedback
- No code written for Rahul — guide, review, explain the WHY behind errors
- Same approach as DevOps project: learn by doing

## Current progress

| Phase | Topic | Status |
|---|---|---|
| 1 | Variables, Data Types, Functions, *args/**kwargs | COMPLETE |
| 2 | OOP — Classes, Inheritance, @property | COMPLETE |
| 3 | Decorators, Generators, Lambda, Regex, Multithreading | IN PROGRESS |
| 4 | Testing — pytest, mocking, coverage | Not started |
| 5 | Flask deeper + REST API patterns | Not started |
| 6 | Databases — psycopg2 deeper, SQLAlchemy | Not started |
| 7 | DevOps Python — subprocess, Docker SDK, argparse | Not started |
| 8 | DSA basics | Not started |
| 9 | NumPy, Pandas, Matplotlib | Not started |
| 10 | Data Science + ML | Not started |

## Phase 3 detail

| Topic | Status |
|---|---|
| Decorators (`log_call`, `retry` factory) | COMPLETE |
| Generators (`log_stream`, `paginate`) | COMPLETE |
| Lambda & comprehensions | COMPLETE |
| Regex (`extract_timestamps`, `extract_errors`, `extract_ips`) | COMPLETE |
| Multithreading basics (threading, join, I/O-bound) | COMPLETE (2026-06-01) |
| Multithreading — locks & shared state | COMPLETE (2026-06-04) |
| Multiprocessing | COMPLETE (2026-06-08) |
| asyncio basics | Next up |

## Session notes
- [2026-05-25](Claude-output/session-2026-05-25.md) — Phase 1 complete, Phase 2 OOP in progress
- [2026-05-26](Claude-output/session-2026-05-26.md) — Phase 2 complete, Phase 3 decorators + generators + lambda + regex complete
- [2026-06-01](Claude-output/session-2026-06-01.md) — Phase 3 threading basics complete (phase3_threading.py); locks + multiprocessing + asyncio next
- [2026-06-04](Claude-output/session-2026-06-04.md) — Locks & shared state complete (phase3_locks.py); race condition demonstrated with explicit read/sleep/write pattern; fixed with threading.Lock(); next: multiprocessing
- [2026-06-08](Claude-output/session-2026-06-08.md) — Multiprocessing complete (phase3_multiprocessing.py); GIL, Pool, pool.map, I/O vs CPU-bound distinction; next: asyncio
