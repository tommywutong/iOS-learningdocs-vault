---
title: negotiatedTLSCipherSuite
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlsessiontasktransactionmetrics/negotiatedtlsciphersuite
source_url: 'https://developer.apple.com/documentation/foundation/nsurlsessiontasktransactionmetrics/negotiatedtlsciphersuite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlsessiontasktransactionmetrics/negotiatedtlsciphersuite.json'
content_hash: 'sha256:22e230a497dd37b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# negotiatedTLSCipherSuite

<sub>Instance Property</sub>

The TLS cipher suite the task negotiated with the endpoint for the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (copy, readonly, nullable) NSNumber * negotiatedTLSCipherSuite;
```

## Discussion

This value is a 2-byte sequence in host byte order. See [tls_ciphersuite_t](../../security/tls_ciphersuite_t.md) for possible values. If the task didn’t negotiate an encrypted connection, this value is `nil`.

## See Also

### Accessing transaction characteristics

- [networkProtocolName](../urlsessiontasktransactionmetrics/networkprotocolname.md) — The network protocol used to fetch the resource.
- [remoteAddress](../urlsessiontasktransactionmetrics/remoteaddress.md) — The IP address string of the remote interface for the connection.
- [remotePort](remoteport.md) — The port number of the remote interface for the connection.
- [localAddress](../urlsessiontasktransactionmetrics/localaddress.md) — The IP address string of the local interface for the connection.
- [localPort](localport.md) — The port number of the local interface for the connection.
- [negotiatedTLSProtocolVersion](negotiatedtlsprotocolversion.md) — The TLS protocol version the task negotiated with the endpoint for the connection.
- [cellular](../urlsessiontasktransactionmetrics/iscellular.md) — A Boolean value that indicates whether the connection operates over a cellular interface.
- [expensive](../urlsessiontasktransactionmetrics/isexpensive.md) — A Boolean value that indicates whether the connection operates over an expensive interface.
- [constrained](../urlsessiontasktransactionmetrics/isconstrained.md) — A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [proxyConnection](../urlsessiontasktransactionmetrics/isproxyconnection.md) — A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [reusedConnection](../urlsessiontasktransactionmetrics/isreusedconnection.md) — A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [multipath](../urlsessiontasktransactionmetrics/ismultipath.md) — A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [resourceFetchType](../urlsessiontasktransactionmetrics/resourcefetchtype.md) — A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [ResourceFetchType](../urlsessiontaskmetrics/resourcefetchtype.md) — The manner in which a resource is fetched.
- [domainResolutionProtocol](../urlsessiontasktransactionmetrics/domainresolutionprotocol.md) — DNS protocol used for domain resolution.
