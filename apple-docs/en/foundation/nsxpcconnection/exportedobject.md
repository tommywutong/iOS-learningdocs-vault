---
title: exportedObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/exportedobject
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/exportedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/exportedobject.json'
content_hash: 'sha256:445dfbba434811c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# exportedObject

<sub>Instance Property</sub>

An exported object for the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var exportedObject: Any? { get set }
```

## Discussion

Messages sent to the [- remoteObjectProxy](<../nsxpcproxycreating/remoteobjectproxy().md>) object from the other side of the connection are dispatched to this object. Messages delivered to exported objects are serialized and sent on a non-main queue. The receiver is responsible for handling the messages on a different queue or thread if it is required.

## See Also

### Managing the connection interface

- [serviceName](servicename.md) — The name of the XPC service that this connection was configured to connect to.
- [endpoint](endpoint.md) — If the connection was created with an [NSXPCListenerEndpoint](../nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [exportedInterface](exportedinterface.md) — The [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [remoteObjectInterface](remoteobjectinterface.md) — Defines the [NSXPCInterface](../nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [remoteObjectProxy](remoteobjectproxy.md) — Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).
