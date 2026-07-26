---
title: dispatch_io_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_t.json'
content_hash: 'sha256:a5e7ef6214813b73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_io_t

<sub>Type Alias</sub>

A dispatch I/O channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_io_t = DispatchIO
```

## Discussion

A dispatch I/O channel represents a file descriptor and the asynchronous I/O policies applied to that file descriptor. A dispatch I/O channel is a standard type of dispatch object and may be retained, released, suspended, and resumed accordingly.

## See Also

### Data Types

- [dispatch_group_t](dispatch_group_t.md) — A group of block objects submitted to a queue for asynchronous invocation.
- [dispatch_object_t](dispatch_object_t.md) — A dispatch object.
- [dispatch_queue_attr_t](dispatch_queue_attr_t.md) — Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_serial_executor_t](dispatch_queue_serial_executor_t.md)
- [dispatch_queue_t](dispatch_queue_t.md) — A lightweight object to which your application submits blocks for subsequent execution.
- [dispatch_semaphore_t](dispatch_semaphore_t.md) — A dispatch semaphore object.
