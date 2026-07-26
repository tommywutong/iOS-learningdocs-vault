---
title: Processes and Threads
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processes-and-threads
source_url: 'https://developer.apple.com/documentation/foundation/processes-and-threads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processes-and-threads.json'
content_hash: 'sha256:18e1924a0f494929'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Processes and Threads

<sub>API Collection</sub>

Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.

## Topics

### Run Loop Scheduling

- [RunLoop](runloop.md) — The programmatic interface to objects that manage input sources.
- [Timer](timer.md) — A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.

### Process Info

- [ProcessInfo](processinfo.md) — A collection of information about the current process.

### Threads and Locking

- [Thread](thread.md) — A thread of execution.
- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSLock](nslock.md) — An object that coordinates the operation of multiple threads of execution within the same application.
- [NSRecursiveLock](nsrecursivelock.md) — A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [NSDistributedLock](nsdistributedlock.md) — A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [NSConditionLock](nsconditionlock.md) — A lock that can be associated with specific, user-defined conditions.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.

### Operations

- [OperationQueue](operationqueue.md) — A queue that regulates the execution of operations.
- [Operation](operation.md) — An abstract class that represents the code and data associated with a single task.
- [BlockOperation](blockoperation.md) — An operation that manages the concurrent execution of one or more blocks.

### Scripts and External Tasks

- [Process](process.md) — An object that represents a subprocess of the current process.
- [NSUserScriptTask](nsuserscripttask.md) — An object that executes scripts.
- [NSUserAppleScriptTask](nsuserapplescripttask.md) — An object that executes AppleScript scripts.
- [NSUserAutomatorTask](nsuserautomatortask.md) — An object that executes Automator workflows.
- [NSUserUnixTask](nsuserunixtask.md) — An object that executes unix applications.

## See Also

### Low-Level Utilities

- [XPC](xpc.md) — Manage secure interprocess communication.
- [Object Runtime](object-runtime.md) — Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md) — Use low-level Unix features to manage input and output among files, processes, and the network.
