---
title: preferNoChecksum
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoludp/options/prefernochecksum
source_url: 'https://developer.apple.com/documentation/network/nwprotocoludp/options/prefernochecksum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoludp/options/prefernochecksum.json'
content_hash: 'sha256:199058977df711d6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolUDP](../../nwprotocoludp.md) · [Options](../options.md)

# preferNoChecksum

<sub>Instance Property</sub>

A Boolean that configures the connection to not send UDP checksums.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferNoChecksum: Bool { get set }
```

## Discussion

UDP checksums are optional when the datagrams are sent over IPv4. This option configures UDP to not set checksums on these datagrams, but has no effect on IPv6.

## See Also

### Customizing UDP Connections

- [init()](<init().md>) — Initializes a default set of UDP connection options.
