---
title: 'connectionWithRegisteredName:host:usingNameServer:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/connectionwithregisteredname:host:usingnameserver:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/connectionwithregisteredname:host:usingnameserver:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/connectionwithregisteredname%3Ahost%3Ausingnameserver%3A.json'
content_hash: 'sha256:6448637e39c32d9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# connectionWithRegisteredName:host:usingNameServer:

<sub>Type Method</sub>

Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (instancetype) connectionWithRegisteredName:(NSString *) name host:(NSString *) hostName usingNameServer:(NSPortNameServer *) server;
```

## Parameters

- `name` — The connection name.

- `hostName` — The host name.

- `server` — The name server.

## Return Value

The `NSConnection` object whose send port links it to the `NSConnection` object registered with `server` under `name` on the host named `hostName`.

## Discussion

See [connectionWithRegisteredName:host:](connectionwithregisteredname_host_.md) for more information.

## See Also

### Getting a Remote Object

- [connectionWithRegisteredName:host:](connectionwithregisteredname_host_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxy](rootproxy.md) — The proxy for the root object of the receiver’s peer in another application or thread. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) — Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:usingNameServer:](rootproxyforconnectionwithregisteredname_host_usingnameserver_.md) — Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host. _(deprecated)_
- [remoteObjects](remoteobjects.md) — The local proxies for remote objects that have been received over the connection but not deallocated yet. _(deprecated)_
- [localObjects](localobjects.md) — The local objects that have been sent over the connection and still have proxies at the other end. _(deprecated)_
