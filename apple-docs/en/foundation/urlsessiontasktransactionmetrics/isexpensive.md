---
title: isExpensive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/isexpensive
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/isexpensive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/isexpensive.json'
content_hash: 'sha256:1abc1c360ea8bd18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# isExpensive

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection operates over an expensive interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isExpensive: Bool { get }
```

## Discussion

The system considers an interface expensive if it’s more costly or consumes more power, such as 3G or LTE as compared to ethernet or Wi-Fi. You permit or deny use of expensive interfaces with the [allowsExpensiveNetworkAccess](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) property on [URLSessionConfiguration](../urlsessionconfiguration.md) or [allowsExpensiveNetworkAccess](../urlrequest/allowsexpensivenetworkaccess.md) on [URLRequest](../urlrequest.md).

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
- [constrained](isconstrained.md) — A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [proxyConnection](isproxyconnection.md) — A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [reusedConnection](isreusedconnection.md) — A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [multipath](ismultipath.md) — A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [resourceFetchType](resourcefetchtype.md) — A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [ResourceFetchType](../urlsessiontaskmetrics/resourcefetchtype.md) — The manner in which a resource is fetched.
- [domainResolutionProtocol](domainresolutionprotocol.md) — DNS protocol used for domain resolution.
