---
title: DispatchIO
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio.json'
content_hash: 'sha256:a281be483ddc6cd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchIO

<sub>Class</sub>

An object that manages operations on a file descriptor using either stream-based or random-access semantics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchIO
```

## Relationships

- **Inherits From**: [DispatchObject](dispatchobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Dispatch I/O Object

- [init(type:fileDescriptor:queue:cleanupHandler:)](<dispatchio/init(type_filedescriptor_queue_cleanuphandler_).md>) — Creates a new I/O channel that accesses the specified file descriptor.
- [init(type:path:oflag:mode:queue:cleanupHandler:)](<dispatchio/init(type_path_oflag_mode_queue_cleanuphandler_)-50rb0.md>) — Creates a new I/O channel that accesses the file at the specified path, potentially creating that file in the process.
- [init(type:io:queue:cleanupHandler:)](<dispatchio/init(type_io_queue_cleanuphandler_).md>) — Creates a new I/O channel from an existing I/O channel.
- [StreamType](dispatchio/streamtype.md) — The semantics for accessing the contents of a file descriptor.

### Reading from the File

- [read(offset:length:queue:ioHandler:)](<dispatchio/read(offset_length_queue_iohandler_).md>) — Schedules an asynchronous read operation on the specified channel.
- [read(fromFileDescriptor:maxLength:runningHandlerOn:handler:)](<dispatchio/read(fromfiledescriptor_maxlength_runninghandleron_handler_).md>) — Schedules an asynchronous read operation using the specified file descriptor.

### Writing to the File

- [write(offset:data:queue:ioHandler:)](<dispatchio/write(offset_data_queue_iohandler_).md>) — Schedules an asynchronous write operation for the specified channel.
- [write(toFileDescriptor:data:runningHandlerOn:handler:)](<dispatchio/write(tofiledescriptor_data_runninghandleron_handler_).md>) — Schedules an asynchronous write operation to the specified file descriptor.

### Closing the File

- [close(flags:)](<dispatchio/close(flags_).md>) — Closes the channel to new read and write operations.
- [CloseFlags](dispatchio/closeflags.md) — Additional flags to use when closing an I/O channel.

### Managing the File Descriptor

- [dispatch_io_get_descriptor](dispatchio/filedescriptor.md) — Returns the file descriptor associated with the specified channel.
- [dispatch_io_set_high_water](<dispatchio/setlimit(highwater_).md>) — Sets the maximum number of bytes to process before enqueueing a handler block.
- [dispatch_io_set_low_water](<dispatchio/setlimit(lowwater_).md>) — Sets the minimum number of bytes to process before enqueueing a handler block.
- [setInterval(interval:flags:)](<dispatchio/setinterval(interval_flags_).md>) — Sets the interval, in nanoseconds, at which to invoke the I/O handlers for the channel.
- [IntervalFlags](dispatchio/intervalflags.md) — The desired delivery behavior for interval events.

### Synchronizing File Operations

- [dispatch_io_barrier](<dispatchio/barrier(execute_).md>) — Schedules a barrier operation on the specified channel.

### Initializers

- [init(type:path:oflag:mode:queue:cleanupHandler:)](<dispatchio/init(type_path_oflag_mode_queue_cleanuphandler_)-25rlb.md>)

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.
