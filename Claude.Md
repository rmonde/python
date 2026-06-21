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
| 3 | Decorators, Generators, Lambda, Regex, Multithreading |  COMPLETE |
| 4 | Testing — pytest, mocking, coverage | COMPLETE |
| 5 | Flask deeper + REST API patterns | COMPLETE (2026-06-21) |
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
| asyncio basics | COMPLETE (2026-06-13) |

## Phase 4 detail

| Topic | Status |
|---|---|
| pytest basics — `assert`, naming conventions, test discovery | COMPLETE (2026-06-13) |
| `@pytest.mark.parametrize` — one test logic, multiple input/expected pairs | COMPLETE (2026-06-13) |
| `@pytest.fixture` — shared setup, injected by name, fresh per test | COMPLETE (2026-06-13) |
| `unittest.mock.patch` — replace external dependencies, control return values | COMPLETE (2026-06-13) |
| `pytest-cov` — coverage measurement, term-missing report, 80% floor rule | COMPLETE (2026-06-13) |

## Phase 5 detail

| Topic | Status |
|---|---|
| Blueprints — namespaced routes, `register_blueprint`, `url_prefix` | COMPLETE (2026-06-21) |
| Error handlers — `@app.errorhandler(404/405)`, JSON over HTML | COMPLETE (2026-06-21) |
| `before_request` / `after_request` hooks | COMPLETE (2026-06-21) |
| REST status codes — 200, 201, 400, 404, 405 | COMPLETE (2026-06-21) |
| Input validation — `data.get()`, `not name or not email` | COMPLETE (2026-06-21) |

## Session notes
- [2026-05-25](Claude-output/session-2026-05-25.md) — Phase 1 complete, Phase 2 OOP in progress
- [2026-05-26](Claude-output/session-2026-05-26.md) — Phase 2 complete, Phase 3 decorators + generators + lambda + regex complete
- [2026-06-01](Claude-output/session-2026-06-01.md) — Phase 3 threading basics complete (phase3_threading.py); locks + multiprocessing + asyncio next
- [2026-06-04](Claude-output/session-2026-06-04.md) — Locks & shared state complete (phase3_locks.py); race condition demonstrated with explicit read/sleep/write pattern; fixed with threading.Lock(); next: multiprocessing
- [2026-06-08](Claude-output/session-2026-06-08.md) — Multiprocessing complete (phase3_multiprocessing.py); GIL, Pool, pool.map, I/O vs CPU-bound distinction; next: asyncio
- [2026-06-13](Claude-output/session-2026-06-13.md) — asyncio complete (phase3_asyncio.py); Phase 4 Testing complete (test_utils.py); next: Phase 5 Flask deeper
- [2026-06-21](Claude-output/session-2026-06-21.md) — Phase 5 Flask deeper complete (phase5_flask/); Blueprints, error handlers, hooks, REST patterns; next: Phase 6 Databases
