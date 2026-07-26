---
title: PortDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/portdelegate
source_url: 'https://developer.apple.com/documentation/foundation/portdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portdelegate.json'
content_hash: 'sha256:400474ddf832cef7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PortDelegate

<sub>Protocol</sub>

An interface for handling incoming messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PortDelegate : NSObjectProtocol
```

## Overview

The [PortDelegate](portdelegate.md) protocol defines the optional methods implemented by delegates of [Port](port.md) objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [NSMachPortDelegate](nsmachportdelegate.md)

## Topics

### Handling Port Messages

- [- handlePortMessage:](<portdelegate/handle(__).md>) — Processes a given incoming message on the port.

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
