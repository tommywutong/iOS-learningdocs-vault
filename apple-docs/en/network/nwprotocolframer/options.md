---
title: NWProtocolFramer.Options
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/options
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/options.json'
content_hash: 'sha256:4ea0ec743204ba32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramer](../nwprotocolframer.md)

# NWProtocolFramer.Options

<sub>Class</sub>

A container you use to add your custom protocol to a connection’s protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Relationships

- **Inherits From**: [NWProtocolOptions](../nwprotocoloptions.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Framer Options

- [init(definition:)](<options/init(definition_).md>) — Initializes a set of protocol options with a custom framer definition.

### Subscripts

- [subscript(_:)](<options/subscript(__).md>)

## See Also

### Using Framers with Connections

- [Definition](definition.md) — A custom protocol definition you use to associate messages with protocol options.
- [Message](message.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.
