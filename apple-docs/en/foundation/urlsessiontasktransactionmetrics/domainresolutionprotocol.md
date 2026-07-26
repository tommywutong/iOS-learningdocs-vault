---
title: domainResolutionProtocol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/domainresolutionprotocol
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/domainresolutionprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/domainresolutionprotocol.json'
content_hash: 'sha256:9ed249446fa16f58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# domainResolutionProtocol

<sub>Instance Property</sub>

DNS protocol used for domain resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var domainResolutionProtocol: URLSessionTaskMetrics.DomainResolutionProtocol { get }
```

## See Also

### Accessing transaction characteristics

- [networkProtocolName](networkprotocolname.md) — The network protocol used to fetch the resource.
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
