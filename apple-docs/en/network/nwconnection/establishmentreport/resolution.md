---
title: NWConnection.EstablishmentReport.Resolution
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution.json'
content_hash: 'sha256:6ec6f40479f68504'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [EstablishmentReport](../establishmentreport.md)

# NWConnection.EstablishmentReport.Resolution

<sub>Structure</sub>

A description of a single DNS resolution step.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Resolution
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Measuring Performance

- [duration](resolution/duration.md) — The duration of this resolution step, from when the query was issued to when the response was complete.
- [source](resolution/source-swift.property.md) — The source of the DNS response.
- [Source](resolution/source-swift.enum.md) — Sources that may provide DNS responses.
- [dnsProtocol](resolution/dnsprotocol-swift.property.md) — The transport protocol your connection used for DNS resolution.
- [DNSProtocol](resolution/dnsprotocol-swift.enum.md) — A set of transport protocols connections use for DNS resolution.

### Examining Resolved Endpoints

- [successfulEndpoint](resolution/successfulendpoint.md) — The resolved endpoint that led to the established connection.
- [preferredEndpoint](resolution/preferredendpoint.md) — The resolved endpoint that the connection used for its first connection attempt.
- [endpointCount](resolution/endpointcount.md) — The number of endpoints resolved in this step.

## See Also

### Inspecting Resolution

- [resolutions](resolutions.md) — The array of resolution steps performed during connection establishment, in order from first resolved to last resolved.
