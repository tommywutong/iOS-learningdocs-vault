---
title: DispatchSourceProcess
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprocess
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprocess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprocess.json'
content_hash: 'sha256:c61177eade0b4297'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceProcess

<sub>Protocol</sub>

A dispatch source that monitors an external process for events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceProcess : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeProcessSource(identifier:eventMask:queue:)](<dispatchsource/makeprocesssource(identifier_eventmask_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Process ID

- [handle](dispatchsourceprocess/handle.md) — The process identifier of the process being monitored by the dispatch source.

### Getting the Event Data

- [data](dispatchsourceprocess/data.md) — Data associated with the last process-related event.
- [mask](dispatchsourceprocess/mask.md) — The process events being monitored by the dispatch source.

## See Also

### Creating a Process Source

- [makeProcessSource(identifier:eventMask:queue:)](<dispatchsource/makeprocesssource(identifier_eventmask_queue_).md>) — Creates a new dispatch source object for monitoring the specified process.
- [ProcessEvent](dispatchsource/processevent.md) — Events related to a process.
