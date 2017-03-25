## Python OS using Coroutines

#### Challenges

- Build a multitasking "operating system"
- Use nothing but pure *python* code
- No threads
- No subprocesses
- Use generators / coroutines

#### Motivations

- There has been a lot of recent interest in alternatives to threads (especially due to the GIL)
- Non-blocking and asynchronous I/O
- Example: servers capable of supporting thousands of simultaneous client connections
- A lot of work has focused on event-driven systems or the "Reactor Model" (e.g., Twisted)
- Coroutines are a whole different twist...


### Step 1: Define Tasks

- `pyos1.py`

### Step 2: The Scheduler

- `pyos2.py`

### Step 3: Task Exit

- `taskcrash.py`
- `pyos3.py`

### Step 4: System Calls

- `pyos4.py`

### Step 5: Task Management

- `pyos5.py`
- `pyos6.py` (Task Waiting)

### Interlude: An Echo Server Attempt

- `echobad.py`
- block IO is undesirable

### I/O Waiting

- `pyos7.py` (Polling Task, Read/Write Syscalls)

### Echo Server Example

- `echogood.py`

### Trampolining

- When working with coroutines, you can't write subroutine functions that yield. (suspend)
- The yield statement can only be used to suspend a coroutine at the top-most level.
- There is a solution
    - it can only be done with the assistance of the task scheduler itself.
    - You have to strictly stick to yield statements
    - Involves a trick known as "trampolining"

- `trampoline.py`
- `pyos8.py`
- `echoserver.py`
- `sockwrap.py`
- `echoserver2.py`

### Future topics

- Intertask communication
- Handling of blocking operations (e.g., accessing database)
- Coroutine multitasking and threads
- Error handling
