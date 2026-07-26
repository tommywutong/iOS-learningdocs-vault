---
title: NWConnection.EstablishmentReport.Resolution.DNSProtocol
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution/dnsprotocol-swift.enum.json'
content_hash: 'sha256:88670e32250c210a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [EstablishmentReport](../../establishmentreport.md) · [Resolution](../resolution.md)

# NWConnection.EstablishmentReport.Resolution.DNSProtocol

<sub>Enumeration</sub>

A set of transport protocols connections use for DNS resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DNSProtocol
```

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Resolution Transports

- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.unknown](dnsprotocol-swift.enum/unknown.md) — The DNS response protocol is unknown or not applicable.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.udp](dnsprotocol-swift.enum/udp.md) — The connection used cleartext UDP for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.tcp](dnsprotocol-swift.enum/tcp.md) — The connection used cleartext TCP for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.tls](dnsprotocol-swift.enum/tls.md) — The connection used TLS for DNS resolution.
- [NWConnection.EstablishmentReport.Resolution.DNSProtocol.https](dnsprotocol-swift.enum/https.md) — The connection used HTTPS for DNS resolution.

## See Also

### Measuring Performance

- [duration](duration.md) — The duration of this resolution step, from when the query was issued to when the response was complete.
- [source](source-swift.property.md) — The source of the DNS response.
- [Source](source-swift.enum.md) — Sources that may provide DNS responses.
- [dnsProtocol](dnsprotocol-swift.property.md) — The transport protocol your connection used for DNS resolution.
