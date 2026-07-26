---
title: serviceClass
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/metadata/serviceclass
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/metadata/serviceclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/metadata/serviceclass.json'
content_hash: 'sha256:48fce46897debbc2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolIP](../../nwprotocolip.md) · [Metadata](../metadata.md)

# serviceClass

<sub>Instance Property</sub>

A specific service class to mark on an IP packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var serviceClass: NWParameters.ServiceClass { get set }
```

## See Also

### Related Documentation

- [serviceClass](../../nwparameters/serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.

### Sending IP Options

- [init()](<init().md>) — Initializes an IP packet configuration with default settings.
- [ecn](ecn.md) — A specific Explicit Congestion Notification flag value to set on an IP packet.
- [ECN](../ecn.md) — Flag values for Explicit Congestion Notifications in IP packets.
