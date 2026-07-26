---
title: 'serviceConnectionWithName:rootObject:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/serviceconnectionwithname:rootobject:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/serviceconnectionwithname:rootobject:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/serviceconnectionwithname%3Arootobject%3A.json'
content_hash: 'sha256:57cb4b95df9bb1b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# serviceConnectionWithName:rootObject:

<sub>Type Method</sub>

Creates and returns a new connection object representing a vended service on the default system port name server.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (instancetype) serviceConnectionWithName:(NSString *) name rootObject:(id) root;
```

## Parameters

- `name` — The name of the service you want to publish.

- `root` — The object to use as the root object for the published service. This is the object vended by the connection.

## Return Value

An `NSConnection` object representing the vended service or `nil` if there was a problem setting up the connection object.

## Discussion

This method creates the server-side of a connection object and registers it with the default system port name server. Clients wishing to connect to this service can request a communications port from the same port server and use that port to communicate.

## See Also

### Related Documentation

- [systemDefaultPortNameServer](../nsportnameserver/systemdefaultportnameserver.md) — Returns the single instance of `NSPortNameServer` for the application. _(deprecated)_
- [connectionWithRegisteredName:host:](connectionwithregisteredname_host_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_

### Vending a Service

- [serviceConnectionWithName:rootObject:usingNameServer:](serviceconnectionwithname_rootobject_usingnameserver_.md) — Creates and returns a new connection object representing a vended service on the specified port name server. _(deprecated)_
- [registerName:](registername_.md) — Registers the specified service using with the default system port name server. _(deprecated)_
- [registerName:withNameServer:](registername_withnameserver_.md) — Registers a service with the specified port name server. _(deprecated)_
- [rootObject](rootobject-c.property.md) — The object that the receiver (or its parent) makes available to other applications or threads. _(deprecated)_
