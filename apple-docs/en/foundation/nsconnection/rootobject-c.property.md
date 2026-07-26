---
title: rootObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/rootobject-c.property
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/rootobject-c.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/rootobject-c.property.json'
content_hash: 'sha256:551b499ad70afd83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# rootObject

<sub>Instance Property</sub>

The object that the receiver (or its parent) makes available to other applications or threads.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, nullable) id rootObject;
```

## Discussion

The object that the receiver (or its parent) makes available to other applications or threads, or `nil` if there is no root object.

To get a proxy to this object in another application or thread, invoke the [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) class method with the appropriate arguments.

Changing the root object only affects new connection requests and [rootProxy](rootproxy.md) messages to established `NSConnection` objects—applications that have proxies to the old root object can still send messages through it.

## See Also

### Related Documentation

- [rootProxy](rootproxy.md) — The proxy for the root object of the receiver’s peer in another application or thread. _(deprecated)_

### Vending a Service

- [serviceConnectionWithName:rootObject:usingNameServer:](serviceconnectionwithname_rootobject_usingnameserver_.md) — Creates and returns a new connection object representing a vended service on the specified port name server. _(deprecated)_
- [serviceConnectionWithName:rootObject:](serviceconnectionwithname_rootobject_.md) — Creates and returns a new connection object representing a vended service on the default system port name server. _(deprecated)_
- [registerName:](registername_.md) — Registers the specified service using with the default system port name server. _(deprecated)_
- [registerName:withNameServer:](registername_withnameserver_.md) — Registers a service with the specified port name server. _(deprecated)_
