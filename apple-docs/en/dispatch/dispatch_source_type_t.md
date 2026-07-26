---
title: dispatch_source_type_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_type_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_type_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_type_t.json'
content_hash: 'sha256:cb534a0ee71f87c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_type_t

<sub>Type Alias</sub>

An identifier for the type of system object being monitored by a dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef const struct dispatch_source_type_s * dispatch_source_type_t;
```

## Discussion

Constants of this type represent the class of low-level system object that is being monitored by the dispatch source. Constants of this type are passed as a parameter to [dispatch_source_create](dispatch_source_create.md) and determine how the handle argument is interpreted (as a file descriptor, mach port, signal number, process identifier, etc.) and how the mask argument is interpreted.

## Topics

### Dispatch Source Types

- [DISPATCH_SOURCE_TYPE_TIMER](dispatch_source_type_timer.md) — A type of dispatch source for monitoring a timer.
- [DISPATCH_SOURCE_TYPE_READ](dispatch_source_type_read.md) — A type of dispatch source for monitoring read operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_WRITE](dispatch_source_type_write.md) — A type of dispatch source for monitoring write operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_VNODE](dispatch_source_type_vnode.md) — A type of dispatch source for monitoring changes to a file system object.
- [DISPATCH_SOURCE_TYPE_SIGNAL](dispatch_source_type_signal.md) — A type of dispatch source for monitoring signals.
- [DISPATCH_SOURCE_TYPE_PROC](dispatch_source_type_proc.md) — A type of dispatch source for monitoring a process.
- [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](dispatch_source_type_memorypressure.md) — A type of dispatch source for monitoring memory pressure events.
- [DISPATCH_SOURCE_TYPE_MACH_SEND](dispatch_source_type_mach_send.md) — A type of dispatch source for monitoring a mach send port.
- [DISPATCH_SOURCE_TYPE_MACH_RECV](dispatch_source_type_mach_recv.md) — A type of dispatch source for monitoring a mach receive port.
- [DISPATCH_SOURCE_TYPE_DATA_ADD](dispatch_source_type_data_add.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an AND operator.
- [DISPATCH_SOURCE_TYPE_DATA_OR](dispatch_source_type_data_or.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an OR operator.

## See Also

### Creating a Dispatch Source

- [dispatch_source_create](dispatch_source_create.md) — Creates a new dispatch source to monitor low-level system events.
- [dispatch_source_t](dispatch_source_t.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
