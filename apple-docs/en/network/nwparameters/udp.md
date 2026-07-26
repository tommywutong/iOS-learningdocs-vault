---
title: udp
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/udp
source_url: 'https://developer.apple.com/documentation/network/nwparameters/udp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/udp.json'
content_hash: 'sha256:99dab22852675e7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# udp

<sub>Type Property</sub>

A set of default parameters for connections and listeners that use UDP.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class var udp: NWParameters { get }
```

## See Also

### Creating Parameters

- [tls](tls.md) — A set of default parameters for connections and listeners that use TLS and TCP.
- [tcp](tcp.md) — A set of default parameters for connections and listeners that use TCP.
- [dtls](dtls.md) — A set of default parameters for connections and listeners that use DTLS and UDP.
- [quic(alpn:)](<quic(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [quicDatagram(alpn:)](<quicdatagram(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [init(tls:tcp:)](<init(tls_tcp_).md>) — Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [init(dtls:udp:)](<init(dtls_udp_).md>) — Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [init(quic:)](<init(quic_).md>) — Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](<init().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber:)](<init(customipprotocolnumber_).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [copy()](<copy().md>) — Performs a deep copy of a parameters object.
