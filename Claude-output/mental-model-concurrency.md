# Python Concurrency — Mental Models & Cheat Sheet
*Read before any interview or before writing concurrent code.*

---

## The One-Line Mental Model for Each

| Model | Mental Image | One Line |
|---|---|---|
| **Threading** | One kitchen, multiple chefs sharing the same fridge | Multiple threads, shared memory, one runs at a time (GIL) |
| **Locks** | A key to a shared cupboard — only one chef holds it at a time | Prevents race conditions on shared state |
| **Multiprocessing** | Multiple kitchens, each with its own fridge | Multiple processes, separate memory, truly parallel |
| **asyncio** | One chef who never stands idle — starts pasta, chops while it boils | One thread, switches between tasks at await points |

---

## The GIL — The Most Important Concept

**What it is:** Python's Global Interpreter Lock. An internal lock inside the Python interpreter that allows only **one thread to execute Python bytecode at any given moment**.

**Why it exists:** CPython's memory management (reference counting) is not thread-safe. The GIL protects it.

**What it means in practice:**

| Work type | GIL behaviour | Threading useful? | Multiprocessing useful? |
|---|---|---|---|
| I/O-bound (network, disk, sleep) | Released while waiting | ✅ Yes | ✅ Yes (overkill) |
| CPU-bound (computation, loops) | Held throughout | ❌ No speedup | ✅ Yes |

**Memory hook:** GIL = a talking stick in a meeting. Only the person holding it can speak (execute). During a coffee break (I/O wait), they put it down and anyone can pick it up.

---

## Threading

**Use when:** I/O-bound tasks — HTTP calls, database queries, file reads, sleep.

**Key classes/functions:**
```python
import threading

t = threading.Thread(target=fn, args=(arg,))
t.start()       # start the thread
t.join()        # wait for it to finish
```

**How it works:** Multiple threads exist inside one process, sharing the same memory. The GIL means only one runs Python code at a time, but during I/O waits the GIL releases — so other threads make progress. Net result: faster for I/O-bound work.

**The trap:** Threads share memory → two threads modifying the same variable = race condition.

---

## Locks & Shared State

**Use when:** Multiple threads need to read-modify-write the same variable.

**The race condition pattern:**
```python
current = shared_counter   # read  ← GIL can switch HERE
time.sleep(0)              # another thread reads the same stale value
shared_counter = current + 1  # both write back +1 instead of +2
```

**The fix:**
```python
lock = threading.Lock()   # one lock, shared across all threads

with lock:                # only ONE thread runs this block at a time
    current = shared_counter
    shared_counter = current + 1
```

**Rules:**
- Create the lock ONCE at module level — not inside the function (each thread needs the same lock)
- `with lock:` is preferred over `lock.acquire()` / `lock.release()` — cleaner and safe if exception occurs
- `global` is needed only when **reassigning** a variable (`x = something`), not when mutating it (`.append()`)
- `list.append()` is GIL-safe in CPython — no lock needed. `counter += 1` is NOT — three bytecodes, GIL can switch between them

**High cardinality labels → use `with lock:` around read-modify-write, not just the write.**

---

## Multiprocessing

**Use when:** CPU-bound tasks — data crunching, image processing, ML inference, number-heavy loops.

**Key classes/functions:**
```python
import multiprocessing

with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(fn, list_of_args)  # returns list of return values
    total = sum(results)
```

**How it works:** Each process is a full Python interpreter with its own memory and its own GIL. Truly runs in parallel on multiple CPU cores. No shared state by default — communication must be explicit (Queue, Pipe, return values).

**Rules:**
- Always use `if __name__ == "__main__":` on macOS/Windows — prevents infinite process spawning
- Workers must **return** results — they cannot write to shared variables
- `Pool(processes=N)` — N should be `multiprocessing.cpu_count()` or a fixed number. Don't set it to equal the number of tasks
- Pool is a task queue: when a worker finishes one task, it picks up the next automatically

**The trap:** Thinking you can share a regular Python variable between processes. You can't — each has its own copy. Use `multiprocessing.Queue` or `multiprocessing.Value` if you need to share.

---

## asyncio (Next Session)

**Use when:** Many I/O-bound tasks where you want maximum concurrency without the overhead of threads or processes.

**Mental model:** One chef who never stands idle. Starts pasta (task A), while pasta boils picks up chopping (task B), while chopping finishes checks the sauce (task C). Never doing two things simultaneously, but never idle.

**Key keywords (preview):**
```python
import asyncio

async def fetch_data():      # coroutine — a task that can be paused
    await asyncio.sleep(2)   # pause HERE, let other coroutines run
    return "done"

asyncio.run(main())          # starts the event loop
asyncio.gather(t1, t2, t3)  # runs multiple coroutines concurrently
```

**The `await` keyword = "I'm waiting — someone else can run now."**

**Why it matters for AI/agent work:** Every HTTP call to an LLM API, every tool invocation in an agent loop is I/O-bound. asyncio lets you fire 10 API calls and process whichever responds first — without 10 threads.

---

## Decision Tree — Which Model to Use?

```
Is the task I/O-bound or CPU-bound?
│
├── I/O-bound (network, DB, disk, sleep)
│   ├── Simple, few tasks → Threading
│   ├── Many tasks, modern codebase → asyncio (preferred in new Python)
│   └── Already using async frameworks (FastAPI, aiohttp) → asyncio
│
└── CPU-bound (heavy computation)
    └── Multiprocessing (always)
```

---

## Quick Comparison Table

| | Threading | Multiprocessing | asyncio |
|---|---|---|---|
| Memory | Shared | Separate | Shared (single thread) |
| True parallelism | No (GIL) | Yes | No (single thread) |
| Best for | I/O-bound | CPU-bound | I/O-bound (many tasks) |
| Overhead | Low | High (process startup) | Very low |
| Complexity | Medium | Medium | Higher (async/await syntax) |
| Real-world use | Web servers, scrapers | Data pipelines, ML | APIs, agents, microservices |

---

## Interview Answers to Memorise

**"What is the GIL?"**
→ Python's internal lock that allows only one thread to execute bytecode at a time. It protects CPython's memory management. Released during I/O, held during CPU work.

**"When would you use threading vs multiprocessing?"**
→ Threading for I/O-bound (network/disk — GIL releases during wait). Multiprocessing for CPU-bound (computation — each process has its own GIL, truly parallel).

**"What is a race condition?"**
→ Two threads read the same value, both modify it, both write back — one update is lost. Happens because read-modify-write is three steps, not one atomic operation.

**"How do you fix a race condition?"**
→ `threading.Lock()` — wraps the read-modify-write block so only one thread executes it at a time.

**"Why must multiprocessing code be inside `if __name__ == '__main__'`?"**
→ On macOS/Windows, importing the module spawns a new process, which imports the module again, which spawns another process — infinite loop. The guard prevents this.

---

*Last updated: 2026-06-08 | Next: asyncio basics (phase3_asyncio.py)*
