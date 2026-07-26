---
title: rootProxy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/rootproxy
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/rootproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/rootproxy.json'
content_hash: 'sha256:3f92a0a5579de0e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# rootProxy

<sub>Instance Property</sub>

The proxy for the root object of the receiver’s peer in another application or thread.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, readonly) NSDistantObject * rootProxy;
```

## Discussion

The proxy returned can change between invocations if the peer `NSConnection` object’s root object is changed.

> [!note] Note
> If the `NSConnection` object uses separate send and receive ports and has no peer, when you invoke `rootProxy` it will block for the duration of the reply timeout interval, waiting for a reply.

## See Also

### Related Documentation

- [rootObject](rootobject-c.property.md) — The object that the receiver (or its parent) makes available to other applications or threads. _(deprecated)_

### Getting a Remote Object

- [connectionWithRegisteredName:host:](connectionwithregisteredname_host_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [connectionWithRegisteredName:host:usingNameServer:](connectionwithregisteredname_host_usingnameserver_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) — Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:usingNameServer:](rootproxyforconnectionwithregisteredname_host_usingnameserver_.md) — Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host. _(deprecated)_
- [remoteObjects](remoteobjects.md) — The local proxies for remote objects that have been received over the connection but not deallocated yet. _(deprecated)_
- [localObjects](localobjects.md) — The local objects that have been sent over the connection and still have proxies at the other end. _(deprecated)_
