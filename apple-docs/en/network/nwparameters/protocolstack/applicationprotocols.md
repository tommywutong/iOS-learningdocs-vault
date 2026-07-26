---
title: applicationProtocols
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/protocolstack/applicationprotocols
source_url: 'https://developer.apple.com/documentation/network/nwparameters/protocolstack/applicationprotocols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/protocolstack/applicationprotocols.json'
content_hash: 'sha256:ffa2eaffeaea0243'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [ProtocolStack](../protocolstack.md)

# applicationProtocols

<sub>Instance Property</sub>

The array of application protocol options used by connections and listeners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var applicationProtocols: [NWProtocolOptions] { get set }
```

## Discussion

The array of application protocols is ordered with the closest to the application first, and the closest to the transport protocol last. For example, if you want to run the WebSocket protocol over TLS, the WebSocket protocol should come first, and the TLS protocol should come second.
