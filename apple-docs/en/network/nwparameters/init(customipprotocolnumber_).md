---
title: 'init(customIPProtocolNumber:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/init(customipprotocolnumber:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/init(customipprotocolnumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/init%28customipprotocolnumber%3A%29.json'
content_hash: 'sha256:82d0018ae110ba60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# init(customIPProtocolNumber:)

<sub>Initializer</sub>

Initializes parameters for connections and listeners using a custom IP protocol.

<sub>macOS</sub>

```swift
init(customIPProtocolNumber: UInt8)
```

## Discussion

Creating custom IP protocol connections requires the “com.apple.developer.networking.custom-protocol” entitlement.

## See Also

### Creating Parameters

- [tls](tls.md) — A set of default parameters for connections and listeners that use TLS and TCP.
- [tcp](tcp.md) — A set of default parameters for connections and listeners that use TCP.
- [dtls](dtls.md) — A set of default parameters for connections and listeners that use DTLS and UDP.
- [udp](udp.md) — A set of default parameters for connections and listeners that use UDP.
- [quic(alpn:)](<quic(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [quicDatagram(alpn:)](<quicdatagram(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [init(tls:tcp:)](<init(tls_tcp_).md>) — Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [init(dtls:udp:)](<init(dtls_udp_).md>) — Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [init(quic:)](<init(quic_).md>) — Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](<init().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [copy()](<copy().md>) — Performs a deep copy of a parameters object.
