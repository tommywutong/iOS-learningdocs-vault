---
title: networkProtocolName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/networkprotocolname
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/networkprotocolname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/networkprotocolname.json'
content_hash: 'sha256:8ced81f884324e5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# networkProtocolName

<sub>Instance Property</sub>

The network protocol used to fetch the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var networkProtocolName: String? { get }
```

## Discussion

When a proxy is configured and a tunnel connection is established, this attribute returns the value for the tunneled protocol, which is identified by the ALPN Protocol ID Identification Sequence, as per [RFC 7310](https://tools.ietf.org/html/rfc7301). For example:

- If no proxy is used, and HTTP/2 is negotiated, then `h2` is returned.
- If HTTP/1.1 is used with the proxy, and the tunneled connection is HTTP/2, then `h2` is returned.
- If HTTP/1.1 is used with the proxy, and there’s no tunnel, then `http/1.1` is returned.

## See Also

### Accessing transaction characteristics

- [remoteAddress](remoteaddress.md) — The IP address string of the remote interface for the connection.
- [remotePort](remoteport.md) — The port number of the remote interface for the connection.
- [localAddress](localaddress.md) — The IP address string of the local interface for the connection.
- [localPort](localport.md) — The port number of the local interface for the connection.
- [negotiatedTLSCipherSuite](negotiatedtlsciphersuite.md) — The TLS cipher suite the task negotiated with the endpoint for the connection.
- [negotiatedTLSProtocolVersion](negotiatedtlsprotocolversion.md) — The TLS protocol version the task negotiated with the endpoint for the connection.
- [cellular](iscellular.md) — A Boolean value that indicates whether the connection operates over a cellular interface.
- [expensive](isexpensive.md) — A Boolean value that indicates whether the connection operates over an expensive interface.
- [constrained](isconstrained.md) — A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [proxyConnection](isproxyconnection.md) — A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [reusedConnection](isreusedconnection.md) — A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [multipath](ismultipath.md) — A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [resourceFetchType](resourcefetchtype.md) — A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [ResourceFetchType](../urlsessiontaskmetrics/resourcefetchtype.md) — The manner in which a resource is fetched.
- [domainResolutionProtocol](domainresolutionprotocol.md) — DNS protocol used for domain resolution.
