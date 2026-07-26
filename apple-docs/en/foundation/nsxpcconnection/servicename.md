---
title: serviceName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/servicename
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/servicename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/servicename.json'
content_hash: 'sha256:d2bf8de0dfbe932e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# serviceName

<sub>Instance Property</sub>

The name of the XPC service that this connection was configured to connect to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var serviceName: String? { get }
```

## See Also

### Managing the connection interface

- [endpoint](endpoint.md) — If the connection was created with an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [exportedInterface](exportedinterface.md) — The [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [exportedObject](exportedobject.md) — An exported object for the connection.
- [remoteObjectInterface](remoteobjectinterface.md) — Defines the [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [remoteObjectProxy](remoteobjectproxy.md) — Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).
