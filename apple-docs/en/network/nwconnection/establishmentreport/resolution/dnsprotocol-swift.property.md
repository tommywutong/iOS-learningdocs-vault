---
title: dnsProtocol
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.property.json'
content_hash: 'sha256:3124746c558755d8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [EstablishmentReport](../../establishmentreport.md) · [Resolution](../resolution.md)

# dnsProtocol

<sub>Instance Property</sub>

The transport protocol your connection used for DNS resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dnsProtocol: NWConnection.EstablishmentReport.Resolution.DNSProtocol { get }
```

## See Also

### Measuring Performance

- [duration](duration.md) — The duration of this resolution step, from when the query was issued to when the response was complete.
- [source](source-swift.property.md) — The source of the DNS response.
- [Source](source-swift.enum.md) — Sources that may provide DNS responses.
- [DNSProtocol](dnsprotocol-swift.enum.md) — A set of transport protocols connections use for DNS resolution.
