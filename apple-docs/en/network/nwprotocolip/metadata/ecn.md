---
title: ecn
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/metadata/ecn
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/metadata/ecn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/metadata/ecn.json'
content_hash: 'sha256:e544164c37018194'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolIP](../../nwprotocolip.md) · [Metadata](../metadata.md)

# ecn

<sub>Instance Property</sub>

A specific Explicit Congestion Notification flag value to set on an IP packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ecn: NWProtocolIP.ECN { get set }
```

## See Also

### Sending IP Options

- [init()](<init().md>) — Initializes an IP packet configuration with default settings.
- [ECN](../ecn.md) — Flag values for Explicit Congestion Notifications in IP packets.
- [serviceClass](serviceclass.md) — A specific service class to mark on an IP packet.
