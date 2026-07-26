---
title: URLSessionTaskMetrics.ResourceFetchType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontaskmetrics/resourcefetchtype
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype.json'
content_hash: 'sha256:789ce2e6d94e2251'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskMetrics](../urlsessiontaskmetrics.md)

# URLSessionTaskMetrics.ResourceFetchType

<sub>Enumeration</sub>

The manner in which a resource is fetched.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ResourceFetchType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Fetch types

- [NSURLSessionTaskMetricsResourceFetchTypeUnknown](resourcefetchtype/unknown.md) — The manner in which the resource was fetched could not be determined.
- [NSURLSessionTaskMetricsResourceFetchTypeNetworkLoad](resourcefetchtype/networkload.md) — The resource was loaded over the network.
- [NSURLSessionTaskMetricsResourceFetchTypeServerPush](resourcefetchtype/serverpush.md) — The resource was pushed by the server to the client. _(deprecated)_
- [NSURLSessionTaskMetricsResourceFetchTypeLocalCache](resourcefetchtype/localcache.md) — The resource was retrieved from the local storage.

### Initializers

- [init(rawValue:)](<resourcefetchtype/init(rawvalue_).md>)

## See Also

### Accessing transaction characteristics

- [networkProtocolName](../urlsessiontasktransactionmetrics/networkprotocolname.md) — The network protocol used to fetch the resource.
- [remoteAddress](../urlsessiontasktransactionmetrics/remoteaddress.md) — The IP address string of the remote interface for the connection.
- [remotePort](../urlsessiontasktransactionmetrics/remoteport.md) — The port number of the remote interface for the connection.
- [localAddress](../urlsessiontasktransactionmetrics/localaddress.md) — The IP address string of the local interface for the connection.
- [localPort](../urlsessiontasktransactionmetrics/localport.md) — The port number of the local interface for the connection.
- [negotiatedTLSCipherSuite](../urlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md) — The TLS cipher suite the task negotiated with the endpoint for the connection.
- [negotiatedTLSProtocolVersion](../urlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md) — The TLS protocol version the task negotiated with the endpoint for the connection.
- [cellular](../urlsessiontasktransactionmetrics/iscellular.md) — A Boolean value that indicates whether the connection operates over a cellular interface.
- [expensive](../urlsessiontasktransactionmetrics/isexpensive.md) — A Boolean value that indicates whether the connection operates over an expensive interface.
- [constrained](../urlsessiontasktransactionmetrics/isconstrained.md) — A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [proxyConnection](../urlsessiontasktransactionmetrics/isproxyconnection.md) — A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [reusedConnection](../urlsessiontasktransactionmetrics/isreusedconnection.md) — A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [multipath](../urlsessiontasktransactionmetrics/ismultipath.md) — A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [resourceFetchType](../urlsessiontasktransactionmetrics/resourcefetchtype.md) — A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [domainResolutionProtocol](../urlsessiontasktransactionmetrics/domainresolutionprotocol.md) — DNS protocol used for domain resolution.
