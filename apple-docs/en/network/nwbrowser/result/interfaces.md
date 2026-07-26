---
title: interfaces
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/result/interfaces
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/interfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/interfaces.json'
content_hash: 'sha256:ee0d7f7d84dd8fca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWBrowser](../../nwbrowser.md) · [Result](../result.md)

# interfaces

<sub>Instance Property</sub>

The list of interfaces on which the service was discovered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let interfaces: [NWInterface]
```

## See Also

### Evaluating Browser Results

- [endpoint](endpoint.md) — The discovered service endpoint.
- [metadata](metadata-swift.property.md) — The metadata associated with the discovered service, such as the TXT record.
- [Metadata](metadata-swift.enum.md) — Values associated with discovered services, such as TXT records.
- [NWTXTRecord](../../nwtxtrecord.md) — A dictionary representing a TXT record in a DNS packet.
