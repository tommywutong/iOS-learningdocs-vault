---
title: DispatchSemaphore
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsemaphore
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsemaphore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsemaphore.json'
content_hash: 'sha256:d5d2118b36fec60d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSemaphore

<sub>Class</sub>

An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchSemaphore
```

## Overview

A dispatch semaphore is an efficient implementation of a traditional counting semaphore. Dispatch semaphores call down to the kernel only when the calling thread needs to be blocked. If the calling semaphore does not need to block, no kernel call is made.

You increment a semaphore count by calling the [signal()](<dispatchsemaphore/signal().md>) method, and decrement a semaphore count by calling [wait()](<dispatchsemaphore/wait().md>) or one of its variants that specifies a timeout.

## Relationships

- **Inherits From**: [DispatchObject](dispatchobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Semaphore

- [dispatch_semaphore_create](<dispatchsemaphore/init(value_).md>) — Creates new counting semaphore with an initial value.

### Signaling the Semaphore

- [signal()](<dispatchsemaphore/signal().md>) — Signals (increments) a semaphore.

### Blocking on the Semaphore

- [wait()](<dispatchsemaphore/wait().md>) — Waits for, or decrements, a semaphore.
- [wait(timeout:)](<dispatchsemaphore/wait(timeout_).md>) — Waits for, or decrements, a semaphore.
- [wait(wallTimeout:)](<dispatchsemaphore/wait(walltimeout_).md>) — Waits for, or decrements, a semaphore.

## See Also

### Task Synchronization

- [Dispatch Semaphore](dispatch-semaphore.md) — An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- [Dispatch Barrier](dispatch-barrier.md) — A synchronization point for tasks executing in a concurrent dispatch queue.
