---
title: NWParameters.ProtocolStack
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/protocolstack
source_url: 'https://developer.apple.com/documentation/network/nwparameters/protocolstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/protocolstack.json'
content_hash: 'sha256:7d7fcbfb8f6067f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# NWParameters.ProtocolStack

<sub>Class</sub>

An ordered set of protocol options that define the protocols that connections and listeners use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ProtocolStack
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Adding Application Protocols

- [applicationProtocols](protocolstack/applicationprotocols.md) — The array of application protocol options used by connections and listeners.

### Configuring Lower Protocols

- [transportProtocol](protocolstack/transportprotocol.md) — The transport protocol options used by connections and listeners.
- [internetProtocol](protocolstack/internetprotocol.md) — The Internet Protocol options used by connections and listeners.

## See Also

### Modifying Protocol Stacks

- [defaultProtocolStack](defaultprotocolstack.md) — The protocol stack used by connections and listeners.
- [NWProtocol](../nwprotocol.md) — The abstract superclass used by Network framework protocols and by custom network protocols that you define.
