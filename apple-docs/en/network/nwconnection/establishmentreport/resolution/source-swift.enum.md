---
title: NWConnection.EstablishmentReport.Resolution.Source
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution/source-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/source-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution/source-swift.enum.json'
content_hash: 'sha256:7dc16e33830a0baa'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [EstablishmentReport](../../establishmentreport.md) · [Resolution](../resolution.md)

# NWConnection.EstablishmentReport.Resolution.Source

<sub>Enumeration</sub>

Sources that may provide DNS responses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Source
```

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Resolution Sources

- [NWConnection.EstablishmentReport.Resolution.Source.query](source-swift.enum/query.md) — The DNS response was received from the network.
- [NWConnection.EstablishmentReport.Resolution.Source.cache](source-swift.enum/cache.md) — The DNS response was retrieved from a local cache.
- [NWConnection.EstablishmentReport.Resolution.Source.expiredCache](source-swift.enum/expiredcache.md) — The DNS response had expired and was retrieved from a local cache.

## See Also

### Measuring Performance

- [duration](duration.md) — The duration of this resolution step, from when the query was issued to when the response was complete.
- [source](source-swift.property.md) — The source of the DNS response.
- [dnsProtocol](dnsprotocol-swift.property.md) — The transport protocol your connection used for DNS resolution.
- [DNSProtocol](dnsprotocol-swift.enum.md) — A set of transport protocols connections use for DNS resolution.
