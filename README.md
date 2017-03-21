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
