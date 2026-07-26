---
title: duration
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution/duration
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution/duration.json'
content_hash: 'sha256:9b15b1fdf4a96632'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [EstablishmentReport](../../establishmentreport.md) · [Resolution](../resolution.md)

# duration

<sub>Instance Property</sub>

The duration of this resolution step, from when the query was issued to when the response was complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let duration: TimeInterval
```

## See Also

### Measuring Performance

- [source](source-swift.property.md) — The source of the DNS response.
- [Source](source-swift.enum.md) — Sources that may provide DNS responses.
- [dnsProtocol](dnsprotocol-swift.property.md) — The transport protocol your connection used for DNS resolution.
- [DNSProtocol](dnsprotocol-swift.enum.md) — A set of transport protocols connections use for DNS resolution.
