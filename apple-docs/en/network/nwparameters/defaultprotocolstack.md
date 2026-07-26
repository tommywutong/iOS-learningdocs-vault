---
title: defaultProtocolStack
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/defaultprotocolstack
source_url: 'https://developer.apple.com/documentation/network/nwparameters/defaultprotocolstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/defaultprotocolstack.json'
content_hash: 'sha256:4ebe4df83c34b733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# defaultProtocolStack

<sub>Instance Property</sub>

The protocol stack used by connections and listeners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var defaultProtocolStack: NWParameters.ProtocolStack { get }
```

## See Also

### Modifying Protocol Stacks

- [ProtocolStack](protocolstack.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
- [NWProtocol](../nwprotocol.md) — The abstract superclass used by Network framework protocols and by custom network protocols that you define.
