---
title: Dispatch I/O
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-i-o
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-i-o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-i-o.json'
content_hash: 'sha256:9acf5faad4c5c934'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch I/O

<sub>API Collection</sub>

An object that manages operations on a file descriptor using either stream-based or random-access semantics.

## Topics

### Creating a Dispatch I/O Object

- [dispatch_io_t](dispatch_io_t.md) — A dispatch I/O channel.

### Managing the File Descriptor

- [dispatch_io_get_descriptor](dispatchio/filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_low_water](<dispatchio/setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_high_water](<dispatchio/setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.

### Synchronizing File Operations

- [dispatch_io_barrier](<dispatchio/barrier(execute_).md>) — Schedules a barrier operation on the specified channel.

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.
