---
title: DISPATCH_SOURCE_TYPE_VNODE
framework: Dispatch
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_type_vnode
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_type_vnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_type_vnode.json'
content_hash: 'sha256:0e9bda9101e38793'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_SOURCE_TYPE_VNODE

<sub>Macro</sub>

A type of dispatch source for monitoring changes to a file system object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define DISPATCH_SOURCE_TYPE_VNODE
```

## Discussion

A dispatch source that monitors a file descriptor for events defined by `Dispatch Source Vnode Event Flags`. The handle is a file descriptor (`int`). The mask is a mask of desired events from `Dispatch Source Vnode Event Flags`.

## See Also

### Dispatch Source Types

- [DISPATCH_SOURCE_TYPE_TIMER](dispatch_source_type_timer.md) — A type of dispatch source for monitoring a timer.
- [DISPATCH_SOURCE_TYPE_READ](dispatch_source_type_read.md) — A type of dispatch source for monitoring read operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_WRITE](dispatch_source_type_write.md) — A type of dispatch source for monitoring write operations on a file descriptor.
- [DISPATCH_SOURCE_TYPE_SIGNAL](dispatch_source_type_signal.md) — A type of dispatch source for monitoring signals.
- [DISPATCH_SOURCE_TYPE_PROC](dispatch_source_type_proc.md) — A type of dispatch source for monitoring a process.
- [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](dispatch_source_type_memorypressure.md) — A type of dispatch source for monitoring memory pressure events.
- [DISPATCH_SOURCE_TYPE_MACH_SEND](dispatch_source_type_mach_send.md) — A type of dispatch source for monitoring a mach send port.
- [DISPATCH_SOURCE_TYPE_MACH_RECV](dispatch_source_type_mach_recv.md) — A type of dispatch source for monitoring a mach receive port.
- [DISPATCH_SOURCE_TYPE_DATA_ADD](dispatch_source_type_data_add.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an AND operator.
- [DISPATCH_SOURCE_TYPE_DATA_OR](dispatch_source_type_data_or.md) — A type of dispatch source for monitoring custom events involving the coalescing of data with an OR operator.
