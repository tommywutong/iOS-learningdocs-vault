---
title: initialMaxStreamDataBidirectionalLocal
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/options/initialmaxstreamdatabidirectionallocal
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/options/initialmaxstreamdatabidirectionallocal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/options/initialmaxstreamdatabidirectionallocal.json'
content_hash: 'sha256:b1edb3ce524d474a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolQUIC](../../nwprotocolquic.md) · [Options](../options.md)

# initialMaxStreamDataBidirectionalLocal

<sub>Instance Property</sub>

A QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var initialMaxStreamDataBidirectionalLocal: Int { get set }
```

## Discussion

This property determines the value of the `initial_max_stream_data_bidi_local` transport parameter.

## See Also

### Customizing Connection Options

- [init(alpn:)](<init(alpn_).md>) — Initializes a default set of QUIC options along with a set of supported Application-Layer Protocol Negotiation values.
- [init()](<init().md>) — Initializes a default set of QUIC options, without specifying a set of supported Application-Layer Protocol Negotiation values.
- [alpn](alpn.md) — A set of supported Application-Layer Protocol Negotiation values.
- [idleTimeout](idletimeout.md) — The idle timeout for the QUIC connection, in milliseconds.
- [initialMaxData](initialmaxdata.md) — A QUIC connection’s initial maximum data transport parameter.
- [initialMaxStreamDataBidirectionalRemote](initialmaxstreamdatabidirectionalremote.md) — A QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [initialMaxStreamDataUnidirectional](initialmaxstreamdataunidirectional.md) — A QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [initialMaxStreamsBidirectional](initialmaxstreamsbidirectional.md) — A QUIC connection’s initial maximum number of bidirectional streams.
- [initialMaxStreamsUnidirectional](initialmaxstreamsunidirectional.md) — A QUIC connection’s initial maximum number of unidirectional streams.
- [maxDatagramFrameSize](maxdatagramframesize.md) — A QUIC connection’s maximum DATAGRAM frame size.
- [maxUDPPayloadSize](maxudppayloadsize.md) — The maximum length of a QUIC packet that can be received on a connection, in bytes.
- [securityProtocolOptions](securityprotocoloptions.md) — The handshake security options QUIC uses.
