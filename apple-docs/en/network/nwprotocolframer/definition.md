---
title: NWProtocolFramer.Definition
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/definition
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/definition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/definition.json'
content_hash: 'sha256:de74ea17eae8e8ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramer](../nwprotocolframer.md)

# NWProtocolFramer.Definition

<sub>Class</sub>

A custom protocol definition you use to associate messages with protocol options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Definition
```

## Relationships

- **Inherits From**: [NWProtocolDefinition](../nwprotocoldefinition.md)

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Defining Framer Protocols

- [init(implementation:)](<definition/init(implementation_).md>) — Initializes a new protocol definition based on your protocol implementation.

## See Also

### Using Framers with Connections

- [Options](options.md) — A container you use to add your custom protocol to a connection’s protocol stack.
- [Message](message.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.
