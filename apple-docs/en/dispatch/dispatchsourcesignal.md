---
title: DispatchSourceSignal
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcesignal
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcesignal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcesignal.json'
content_hash: 'sha256:629035a14aa1527a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceSignal

<sub>Protocol</sub>

A dispatch source that monitors the current process for UNIX signals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceSignal : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeSignalSource(signal:queue:)](<dispatchsource/makesignalsource(signal_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## See Also

### Creating a Signal Source

- [makeSignalSource(signal:queue:)](<dispatchsource/makesignalsource(signal_queue_).md>) — Creates a new dispatch source object that monitors the arrival of a UNIX signal.
