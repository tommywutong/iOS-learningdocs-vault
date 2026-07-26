---
title: NWConnection.EstablishmentReport.Handshake
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/handshake
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/handshake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/handshake.json'
content_hash: 'sha256:046921d17bfb2b23'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [EstablishmentReport](../establishmentreport.md)

# NWConnection.EstablishmentReport.Handshake

<sub>Structure</sub>

A description of a single protocol handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Handshake
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Measuring Performance

- [handshakeDuration](handshake/handshakeduration.md) — The duration of the protocol handshake.
- [handshakeRTT](handshake/handshakertt.md) — The round-trip time the protocol observed during its handshake.

### Identifying Protocols

- [definition](handshake/definition.md) — The protocol performing the handshake.

## See Also

### Inspecting Protocol Handshakes

- [handshakes](handshakes.md) — The array of protocol handshakes in order from first completed to last completed.
