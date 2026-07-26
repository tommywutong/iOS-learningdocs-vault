---
title: NWProtocol
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocol
source_url: 'https://developer.apple.com/documentation/network/nwprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocol.json'
content_hash: 'sha256:4b10f9c334f00e59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocol

<sub>Class</sub>

The abstract superclass used by Network framework protocols and by custom network protocols that you define.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocol
```

## Relationships

- **Inherited By**: [NWProtocolFramer](nwprotocolframer.md), [NWProtocolIP](nwprotocolip.md), [NWProtocolQUIC](nwprotocolquic.md), [NWProtocolTCP](nwprotocoltcp.md), [NWProtocolTLS](nwprotocoltls.md), [NWProtocolUDP](nwprotocoludp.md), [NWProtocolWebSocket](nwprotocolwebsocket.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Adding Protocols to Connections

- [NWProtocolOptions](nwprotocoloptions.md) — The abstract superclass for configuring the options of a network protocol.
- [NWProtocolDefinition](nwprotocoldefinition.md) — The abstract superclass for identifying a network protocol.

### Interacting with Protocols

- [NWProtocolMetadata](nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.

## See Also

### Modifying Protocol Stacks

- [defaultProtocolStack](nwparameters/defaultprotocolstack.md) — The protocol stack used by connections and listeners.
- [ProtocolStack](nwparameters/protocolstack.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
