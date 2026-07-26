---
title: remoteMaxStreamsUnidirectional
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/metadata/remotemaxstreamsunidirectional
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/metadata/remotemaxstreamsunidirectional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/metadata/remotemaxstreamsunidirectional.json'
content_hash: 'sha256:42e6d7e51ed59fa3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolQUIC](../../nwprotocolquic.md) · [Metadata](../metadata.md)

# remoteMaxStreamsUnidirectional

<sub>Instance Property</sub>

The maximum number of unidirectional streams advertised by peer that the connection is allowed to create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var remoteMaxStreamsUnidirectional: Int { get }
```

## See Also

### Inspecting Connection State

- [negotiatedALPN](negotiatedalpn.md) — The Application-Layer Protocol Negotiation value used when establishing the connection.
- [localMaxStreamsBidirectional](localmaxstreamsbidirectional.md) — The maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [localMaxStreamsUnidirectional](localmaxstreamsunidirectional.md) — The maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [remoteMaxStreamsBidirectional](remotemaxstreamsbidirectional.md) — The maximum number of bidirectional streams advertised by peer that the connection is allowed to create.
- [remoteIdleTimeout](remoteidletimeout.md) — The idle timeout value from the peer’s transport parameters, in milliseconds.
- [securityProtocolMetadata](securityprotocolmetadata.md) — The result of the QUIC handshake.
