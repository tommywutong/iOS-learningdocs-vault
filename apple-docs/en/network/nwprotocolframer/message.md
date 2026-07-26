---
title: NWProtocolFramer.Message
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/message
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/message.json'
content_hash: 'sha256:7cacb50c2e551cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramer](../nwprotocolframer.md)

# NWProtocolFramer.Message

<sub>Class</sub>

A message for a custom protocol, in which you can store arbitrary key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Message
```

## Relationships

- **Inherits From**: [NWProtocolMetadata](../nwprotocolmetadata.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Framer Messages

- [init(definition:)](<message/init(definition_).md>) — Initializes an empty message for a custom framer definition.
- [init(instance:)](<message/init(instance_).md>) — Initializes an empty message from within a framer implementation.

### Accessing Message Metadata

- [subscript(_:)](<message/subscript(__).md>) — Get and set object values in a custom framer message.

## See Also

### Using Framers with Connections

- [Definition](definition.md) — A custom protocol definition you use to associate messages with protocol options.
- [Options](options.md) — A container you use to add your custom protocol to a connection’s protocol stack.
