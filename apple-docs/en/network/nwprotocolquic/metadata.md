---
title: NWProtocolQUIC.Metadata
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/metadata
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/metadata.json'
content_hash: 'sha256:4742abfcd29eebfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolQUIC](../nwprotocolquic.md)

# NWProtocolQUIC.Metadata

<sub>Class</sub>

A handle you can use to inspect a connection’s QUIC state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Metadata
```

## Relationships

- **Inherits From**: [NWProtocolMetadata](../nwprotocolmetadata.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting Connection State

- [negotiatedALPN](metadata/negotiatedalpn.md) — The Application-Layer Protocol Negotiation value used when establishing the connection.
- [localMaxStreamsBidirectional](metadata/localmaxstreamsbidirectional.md) — The maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [localMaxStreamsUnidirectional](metadata/localmaxstreamsunidirectional.md) — The maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [remoteMaxStreamsBidirectional](metadata/remotemaxstreamsbidirectional.md) — The maximum number of bidirectional streams advertised by peer that the connection is allowed to create.
- [remoteMaxStreamsUnidirectional](metadata/remotemaxstreamsunidirectional.md) — The maximum number of unidirectional streams advertised by peer that the connection is allowed to create.
- [remoteIdleTimeout](metadata/remoteidletimeout.md) — The idle timeout value from the peer’s transport parameters, in milliseconds.
- [securityProtocolMetadata](metadata/securityprotocolmetadata.md) — The result of the QUIC handshake.

### Inspecting Stream State

- [streamIdentifier](metadata/streamidentifier.md) — The QUIC stream identifier.
- [usableDatagramFrameSize](metadata/usabledatagramframesize.md) — The maximum usable size of a datagram frame on a QUIC datagram flow.

### Handling Errors

- [applicationError](metadata/applicationerror.md) — The QUIC application error code to send for the connection, or received from the peer.
- [ApplicationError](applicationerror.md) — A QUIC application error code.
- [streamApplicationErrorCode](metadata/streamapplicationerrorcode.md) — The QUIC application error code to send for the stream, or received from the peer.

### Configuring Keepalives

- [keepAlive](metadata/keepalive.md) — The QUIC connection keepalive behavior.
- [KeepAliveBehavior](metadata/keepalivebehavior.md) — A QUIC connection keepalive behavior.
