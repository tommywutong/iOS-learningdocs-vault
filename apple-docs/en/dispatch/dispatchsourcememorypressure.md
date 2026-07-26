---
title: DispatchSourceMemoryPressure
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcememorypressure
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcememorypressure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcememorypressure.json'
content_hash: 'sha256:e966af9b41ac28e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceMemoryPressure

<sub>Protocol</sub>

A dispatch source that monitors the system for changes in the memory pressure condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceMemoryPressure : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeMemoryPressureSource(eventMask:queue:)](<dispatchsource/makememorypressuresource(eventmask_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Event Data

- [data](dispatchsourcememorypressure/data.md)
- [mask](dispatchsourcememorypressure/mask.md)

## See Also

### Creating a Memory Pressure Source

- [makeMemoryPressureSource(eventMask:queue:)](<dispatchsource/makememorypressuresource(eventmask_queue_).md>) — Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [MemoryPressureEvent](dispatchsource/memorypressureevent.md) — Memory pressure events.
