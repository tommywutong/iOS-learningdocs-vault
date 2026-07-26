---
title: DispatchSource
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource.json'
content_hash: 'sha256:4d45ee26d340c811'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSource

<sub>Class</sub>

An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchSource
```

## Overview

Use the methods of this class to construct new dispatch sources of the appropriate types.

## Relationships

- **Inherits From**: [DispatchObject](dispatchobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md), [DispatchSourceMachReceive](dispatchsourcemachreceive.md), [DispatchSourceMachSend](dispatchsourcemachsend.md), [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md), [DispatchSourceProcess](dispatchsourceprocess.md), [DispatchSourceProtocol](dispatchsourceprotocol.md), [DispatchSourceRead](dispatchsourceread.md), [DispatchSourceSignal](dispatchsourcesignal.md), [DispatchSourceTimer](dispatchsourcetimer.md), [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md), [DispatchSourceUserDataOr](dispatchsourceuserdataor.md), [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md), [DispatchSourceWrite](dispatchsourcewrite.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing Common Dispatch Source Properties

- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.

### Creating a Timer Source

- [makeTimerSource(flags:queue:)](<dispatchsource/maketimersource(flags_queue_).md>) — Creates a new dispatch source object for monitoring timer events.
- [DispatchSourceTimer](dispatchsourcetimer.md) — A dispatch source that submits the event handler block based on a timer.
- [TimerFlags](dispatchsource/timerflags.md) — Flags to use when configuring a timer dispatch source.

### Creating a File System Source

- [makeReadSource(fileDescriptor:queue:)](<dispatchsource/makereadsource(filedescriptor_queue_).md>) — Creates a new dispatch source object for reading bytes from the specified file.
- [makeWriteSource(fileDescriptor:queue:)](<dispatchsource/makewritesource(filedescriptor_queue_).md>) — Creates a new dispatch source object for writing data to the specified file.
- [makeFileSystemObjectSource(fileDescriptor:eventMask:queue:)](<dispatchsource/makefilesystemobjectsource(filedescriptor_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring file-system events.
- [DispatchSourceRead](dispatchsourceread.md) — A dispatch source object for reading data from a file descriptor.
- [DispatchSourceWrite](dispatchsourcewrite.md) — A dispatch source object for writing data to a file descriptor.
- [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md) — A dispatch source that monitors events associated with a file descriptor.
- [FileSystemEvent](dispatchsource/filesystemevent.md) — Events involving a change to a file system object.

### Creating a Process Source

- [makeProcessSource(identifier:eventMask:queue:)](<dispatchsource/makeprocesssource(identifier_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring the specified process.
- [DispatchSourceProcess](dispatchsourceprocess.md) — A dispatch source that monitors an external process for events.
- [ProcessEvent](dispatchsource/processevent.md) — Events related to a process.

### Creating a Memory Pressure Source

- [makeMemoryPressureSource(eventMask:queue:)](<dispatchsource/makememorypressuresource(eventmask_queue_).md>) — Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md) — A dispatch source that monitors the system for changes in the memory pressure condition.
- [MemoryPressureEvent](dispatchsource/memorypressureevent.md) — Memory pressure events.

### Creating a Signal Source

- [makeSignalSource(signal:queue:)](<dispatchsource/makesignalsource(signal_queue_).md>) — Creates a new dispatch source object that monitors the arrival of a UNIX signal.
- [DispatchSourceSignal](dispatchsourcesignal.md) — A dispatch source that monitors the current process for UNIX signals.

### Creating a Mach Port Source

- [makeMachReceiveSource(port:queue:)](<dispatchsource/makemachreceivesource(port_queue_).md>) — Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [makeMachSendSource(port:eventMask:queue:)](<dispatchsource/makemachsendsource(port_eventmask_queue_).md>) — A dispatch source that monitors a Mach port for dead name notifications.
- [DispatchSourceMachReceive](dispatchsourcemachreceive.md) — A dispatch source that monitors a Mach port for pending messages.
- [DispatchSourceMachSend](dispatchsourcemachsend.md) — A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [MachSendEvent](dispatchsource/machsendevent.md) — Mach-related events.

### Creating a Custom Source

- [makeUserDataAddSource(queue:)](<dispatchsource/makeuserdataaddsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [makeUserDataOrSource(queue:)](<dispatchsource/makeuserdataorsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [makeUserDataReplaceSource(queue:)](<dispatchsource/makeuserdatareplacesource(queue_).md>) — Creates a new dispatch source object that you use to track custom app data.
- [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md) — A dispatch source that coalesces data you provide using an AND operation.
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md) — A dispatch source that coalesces data you provide using an OR operation.
- [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md) — A dispatch source that replaces any pending data with the new value you provide.

## See Also

### System Event Monitoring

- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.
