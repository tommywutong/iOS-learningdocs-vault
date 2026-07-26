---
title: 'init(tls:tcp:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/init(tls:tcp:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/init(tls:tcp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/init%28tls%3Atcp%3A%29.json'
content_hash: 'sha256:8a218a79a43686f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# init(tls:tcp:)

<sub>Initializer</sub>

Initializes parameters for TLS connections and listeners with custom TLS and TCP options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(tls: NWProtocolTLS.Options?, tcp: NWProtocolTCP.Options = NWProtocolTCP.Options())
```

## See Also

### Creating Parameters

- [tls](tls.md) — A set of default parameters for connections and listeners that use TLS and TCP.
- [tcp](tcp.md) — A set of default parameters for connections and listeners that use TCP.
- [dtls](dtls.md) — A set of default parameters for connections and listeners that use DTLS and UDP.
- [udp](udp.md) — A set of default parameters for connections and listeners that use UDP.
- [quic(alpn:)](<quic(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [quicDatagram(alpn:)](<quicdatagram(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [init(dtls:udp:)](<init(dtls_udp_).md>) — Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [init(quic:)](<init(quic_).md>) — Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](<init().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber:)](<init(customipprotocolnumber_).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [copy()](<copy().md>) — Performs a deep copy of a parameters object.
