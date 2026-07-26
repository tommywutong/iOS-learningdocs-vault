---
title: DispatchSourceProtocol
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprotocol
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol.json'
content_hash: 'sha256:976e66631cd813f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceProtocol

<sub>Protocol</sub>

Defines a common set of properties and methods that are shared with all dispatch source types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceProtocol : NSObjectProtocol
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeSignalSource(signal:queue:)](<dispatchsource/makesignalsource(signal_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [DispatchSourceFileSystemObject](dispatchsourcefilesystemobject.md), [DispatchSourceMachReceive](dispatchsourcemachreceive.md), [DispatchSourceMachSend](dispatchsourcemachsend.md), [DispatchSourceMemoryPressure](dispatchsourcememorypressure.md), [DispatchSourceProcess](dispatchsourceprocess.md), [DispatchSourceRead](dispatchsourceread.md), [DispatchSourceSignal](dispatchsourcesignal.md), [DispatchSourceTimer](dispatchsourcetimer.md), [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md), [DispatchSourceUserDataOr](dispatchsourceuserdataor.md), [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md), [DispatchSourceWrite](dispatchsourcewrite.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Activating, Suspending, and Resuming a Source

- [activate()](<dispatchsourceprotocol/activate().md>) — Activates the dispatch source.
- [suspend()](<dispatchsourceprotocol/suspend().md>) — Suspends the dispatch source.
- [resume()](<dispatchsourceprotocol/resume().md>) — Resumes the dispatch source.

### Canceling a Dispatch Source

- [cancel()](<dispatchsourceprotocol/cancel().md>) — Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [isCancelled](dispatchsourceprotocol/iscancelled.md) — Returns a Boolean indicating whether the given dispatch source has been canceled.
- [setCancelHandler(handler:)](<dispatchsourceprotocol/setcancelhandler(handler_).md>) — Sets the cancellation handler block for the dispatch source.
- [setCancelHandler(qos:flags:handler:)](<dispatchsourceprotocol/setcancelhandler(qos_flags_handler_).md>) — Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.

### Installing Event Handlers

- [setEventHandler(handler:)](<dispatchsourceprotocol/seteventhandler(handler_).md>) — Sets the event handler work item for the dispatch source.
- [setEventHandler(qos:flags:handler:)](<dispatchsourceprotocol/seteventhandler(qos_flags_handler_).md>)
- [setRegistrationHandler(handler:)](<dispatchsourceprotocol/setregistrationhandler(handler_).md>) — Sets the registration handler work item for the dispatch source.
- [setRegistrationHandler(qos:flags:handler:)](<dispatchsourceprotocol/setregistrationhandler(qos_flags_handler_).md>)
- [DispatchSourceHandler](dispatchsourceprotocol/dispatchsourcehandler.md)

### Getting the Dispatch Source Attributes

- [handle](dispatchsourceprotocol/handle.md) — Returns the underlying system handle associated with the specified dispatch source.
- [data](dispatchsourceprotocol/data.md) — Returns pending data for the dispatch source.
- [mask](dispatchsourceprotocol/mask.md) — Returns the mask of events monitored by the dispatch source.

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchData](dispatchdata.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
