---
title: Dispatch Semaphore
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-semaphore
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-semaphore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-semaphore.json'
content_hash: 'sha256:4935da2b1d3c629e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch Semaphore

<sub>API Collection</sub>

An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.

## Overview

A dispatch semaphore is an efficient implementation of a traditional counting semaphore. Dispatch semaphores call down to the kernel only when the calling thread needs to be blocked. If the calling semaphore does not need to block, no kernel call is made.

You increment a semaphore count by calling the [signal()](<dispatchsemaphore/signal().md>) method, and decrement a semaphore count by calling [dispatch_semaphore_wait](dispatch_semaphore_wait.md) or one of its variants that specifies a timeout.

## Topics

### Creating a Semaphore

- [dispatch_semaphore_create](<dispatchsemaphore/init(value_).md>) — Creates new counting semaphore with an initial value.
- [dispatch_semaphore_t](dispatch_semaphore_t.md) — A dispatch semaphore object.

## See Also

### Task Synchronization

- [DispatchSemaphore](dispatchsemaphore.md) — An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](dispatch-barrier.md) — A synchronization point for tasks executing in a concurrent dispatch queue.
