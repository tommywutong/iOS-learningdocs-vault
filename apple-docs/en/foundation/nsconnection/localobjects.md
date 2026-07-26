---
title: localObjects
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/localobjects
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/localobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/localobjects.json'
content_hash: 'sha256:2aba73b627540624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# localObjects

<sub>Instance Property</sub>

The local objects that have been sent over the connection and still have proxies at the other end.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (copy, readonly) NSArray * localObjects;
```

## Discussion

When an object’s remote proxy is deallocated, a message is sent back to the receiver to notify it that the local object is no longer shared over the connection.

## See Also

### Getting a Remote Object

- [connectionWithRegisteredName:host:](connectionwithregisteredname_host_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [connectionWithRegisteredName:host:usingNameServer:](connectionwithregisteredname_host_usingnameserver_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host. _(deprecated)_
- [rootProxy](rootproxy.md) — The proxy for the root object of the receiver’s peer in another application or thread. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) — Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:usingNameServer:](rootproxyforconnectionwithregisteredname_host_usingnameserver_.md) — Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host. _(deprecated)_
- [remoteObjects](remoteobjects.md) — The local proxies for remote objects that have been received over the connection but not deallocated yet. _(deprecated)_
