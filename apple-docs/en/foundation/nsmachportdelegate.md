---
title: NSMachPortDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachportdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsmachportdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachportdelegate.json'
content_hash: 'sha256:320d66245b287184'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMachPortDelegate

<sub>Protocol</sub>

An interface for handling incoming Mach messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSMachPortDelegate : PortDelegate
```

## Overview

Delegates of [NSMachPort](nsmachport.md) objects optionally adopt this protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [PortDelegate](portdelegate.md)

## Topics

### Handling Mach messages

- [- handleMachMessage:](<nsmachportdelegate/handlemachmessage(__).md>) — Process an incoming Mach message.

## See Also

### Legacy

- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
