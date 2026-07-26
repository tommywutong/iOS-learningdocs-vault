---
title: MessagePort
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/messageport
source_url: 'https://developer.apple.com/documentation/foundation/messageport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/messageport.json'
content_hash: 'sha256:f0c989d4c80b0166'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MessagePort

<sub>Class</sub>

A port that can be used as an endpoint for distributed object connections (or raw messaging).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MessagePort
```

## Overview

[MessagePort](messageport.md) is a subclass of [Port](port.md) that allows for local (on the same machine) communication only. A companion class, [SocketPort](socketport.md), allows for both local and remote communication, but may be more expensive than [MessagePort](messageport.md) for the local case.

[MessagePort](messageport.md) defines no additional methods over those already defined by [Port](port.md).

> [!note] Note
> [MessagePort](messageport.md) conforms to the [NSCoding](nscoding.md) protocol, but only supports coding by an [NSPortCoder](nsportcoder.md) object. [Port](port.md) and its subclasses do not support archiving.

> [!important] Important
> Avoid [MessagePort](messageport.md). There’s little reason to use [MessagePort](messageport.md) rather than [NSMachPort](nsmachport.md) or [SocketPort](socketport.md). There’s no particular performance or functionality advantage. It is recommended avoiding its use.
>
> [MessagePort](messageport.md) may be deprecated in the macOS 10.6 or later.

## Relationships

- **Inherits From**: [Port](port.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
