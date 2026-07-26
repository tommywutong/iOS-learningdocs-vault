---
title: endpoint
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/endpoint
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/endpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/endpoint.json'
content_hash: 'sha256:bed3784bb1a50e29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# endpoint

<sub>Instance Property</sub>

If the connection was created with an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object, returns the endpoint object used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endpoint: NSXPCListenerEndpoint { get }
```

## See Also

### Managing the connection interface

- [serviceName](servicename.md) — The name of the XPC service that this connection was configured to connect to.
- [exportedInterface](exportedinterface.md) — The [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [exportedObject](exportedobject.md) — An exported object for the connection.
- [remoteObjectInterface](remoteobjectinterface.md) — Defines the [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [remoteObjectProxy](remoteobjectproxy.md) — Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).
