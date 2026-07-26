---
title: remoteObjectProxy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/remoteobjectproxy
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/remoteobjectproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/remoteobjectproxy.json'
content_hash: 'sha256:5c46425ac7c1e037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# remoteObjectProxy

<sub>Instance Property</sub>

Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var remoteObjectProxy: Any { get }
```

## Discussion

See descriptions in [NSXPCProxyCreating](../nsxpcproxycreating.md) for more details.

## See Also

### Managing the connection interface

- [serviceName](servicename.md) — The name of the XPC service that this connection was configured to connect to.
- [endpoint](endpoint.md) — If the connection was created with an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [exportedInterface](exportedinterface.md) — The [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [exportedObject](exportedobject.md) — An exported object for the connection.
- [remoteObjectInterface](remoteobjectinterface.md) — Defines the [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
