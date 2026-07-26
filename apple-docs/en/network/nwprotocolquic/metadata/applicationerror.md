---
title: applicationError
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/metadata/applicationerror
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/metadata/applicationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/metadata/applicationerror.json'
content_hash: 'sha256:9802d5985547b4b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolQUIC](../../nwprotocolquic.md) · [Metadata](../metadata.md)

# applicationError

<sub>Instance Property</sub>

The QUIC application error code to send for the connection, or received from the peer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var applicationError: NWProtocolQUIC.ApplicationError { get set }
```

## See Also

### Handling Errors

- [ApplicationError](../applicationerror.md) — A QUIC application error code.
- [streamApplicationErrorCode](streamapplicationerrorcode.md) — The QUIC application error code to send for the stream, or received from the peer.
