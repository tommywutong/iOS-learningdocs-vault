---
title: Dispatch Barrier
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-barrier
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-barrier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-barrier.json'
content_hash: 'sha256:1c7f1f74c00ba4e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch Barrier

<sub>API Collection</sub>

A synchronization point for tasks executing in a concurrent dispatch queue.

## Overview

Use a barrier to synchronize the execution of one or more tasks in your dispatch queue. When you add a barrier to a concurrent dispatch queue, the queue delays the execution of the barrier block (and any tasks submitted after the barrier) until all previously submitted tasks finish executing. After the previous tasks finish executing, the queue executes the barrier block by itself. Once the barrier block finishes, the queue resumes its normal execution behavior.

## See Also

### Task Synchronization

- [DispatchSemaphore](dispatchsemaphore.md) — An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Semaphore](dispatch-semaphore.md) — An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
