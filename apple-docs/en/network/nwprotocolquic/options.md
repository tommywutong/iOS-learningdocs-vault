---
title: NWProtocolQUIC.Options
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/options
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/options.json'
content_hash: 'sha256:9b7e31c072d61b38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolQUIC](../nwprotocolquic.md)

# NWProtocolQUIC.Options

<sub>Class</sub>

A container of options that configure the use of QUIC on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Relationships

- **Inherits From**: [NWProtocolOptions](../nwprotocoloptions.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Customizing Connection Options

- [init(alpn:)](<options/init(alpn_).md>) — Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](<options/init().md>) — Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [alpn](options/alpn.md) — A set of supported Application-Layer Protocol Negotiation values.
- [idleTimeout](options/idletimeout.md) — The idle timeout for the QUIC connection, in milliseconds.
- [initialMaxData](options/initialmaxdata.md) — A QUIC connection’s initial maximum data transport parameter.
- [initialMaxStreamDataBidirectionalLocal](options/initialmaxstreamdatabidirectionallocal.md) — A QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [initialMaxStreamDataBidirectionalRemote](options/initialmaxstreamdatabidirectionalremote.md) — A QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [initialMaxStreamDataUnidirectional](options/initialmaxstreamdataunidirectional.md) — A QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [initialMaxStreamsBidirectional](options/initialmaxstreamsbidirectional.md) — A QUIC connection’s initial maximum number of bidirectional streams.
- [initialMaxStreamsUnidirectional](options/initialmaxstreamsunidirectional.md) — A QUIC connection’s initial maximum number of unidirectional streams.
- [maxDatagramFrameSize](options/maxdatagramframesize.md) — A QUIC connection’s maximum DATAGRAM frame size.
- [maxUDPPayloadSize](options/maxudppayloadsize.md) — The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [securityProtocolOptions](options/securityprotocoloptions.md) — The handshake security options QUIC uses.

### Customizing Stream Options

- [direction](options/direction-swift.property.md) — The direction of the QUIC stream.
- [Direction](options/direction-swift.enum.md) — A directionality of a QUIC stream.
- [isDatagram](options/isdatagram.md) — A Boolean that indicates that this is a QUIC datagram flow, not a stream of bytes.

## See Also

### Creating QUIC Connections

- [definition](definition.md) — The system definition of the QUIC transport protocol.
