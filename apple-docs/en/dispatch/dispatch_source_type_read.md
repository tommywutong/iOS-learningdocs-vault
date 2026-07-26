---
title: DISPATCH_SOURCE_TYPE_READ
framework: Dispatch
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_type_read
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_type_read'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_type_read.json'
content_hash: 'sha256:bb73cba9eff98f31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_SOURCE_TYPE_READ

<sub>Macro</sub>

A type of dispatch source for monitoring read operations on a file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define DISPATCH_SOURCE_TYPE_READ
```

## Discussion

A dispatch source that monitors a file descriptor for pending bytes available to be read. The handle is a file descriptor (`int`). The mask is unused (pass zero for now).

## See Also

### Dispatch Source Types

- [DISPATCH_SOURCE_TYPE_TIMER](dispatch_source_type_timer.md) — A type of dispatch source for monitoring a timer.
- [DISPATCH_SOURCE_TYPE_WRITE](dispatch_source_type_write.md) — A type of dispatch source for monitoring write operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_VNODE](dispatch_source_type_vnode.md) — A type of dispatch source for monitoring changes to a file system object.
- [DISPATCH_SOURCE_TYPE_SIGNAL](dispatch_source_type_signal.md) — A type of dispatch source for monitoring signals.
- [DISPATCH_SOURCE_TYPE_PROC](dispatch_source_type_proc.md) — A type of dispatch source for monitoring a process.
- [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](dispatch_source_type_memorypressure.md) — A type of dispatch source for monitoring memory pressure events.
- [DISPATCH_SOURCE_TYPE_MACH_SEND](dispatch_source_type_mach_send.md) — A type of dispatch source for monitoring a mach send port.
- [DISPATCH_SOURCE_TYPE_MACH_RECV](dispatch_source_type_mach_recv.md) — A type of dispatch source for monitoring a mach receive port.
- [DISPATCH_SOURCE_TYPE_DATA_ADD](dispatch_source_type_data_add.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an AND operator.
- [DISPATCH_SOURCE_TYPE_DATA_OR](dispatch_source_type_data_or.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an OR operator.
