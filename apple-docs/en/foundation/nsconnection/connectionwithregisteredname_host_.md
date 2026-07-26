---
title: 'connectionWithRegisteredName:host:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/connectionwithregisteredname:host:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/connectionwithregisteredname:host:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/connectionwithregisteredname%3Ahost%3A.json'
content_hash: 'sha256:ade0529fc4386a91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# connectionWithRegisteredName:host:

<sub>Type Method</sub>

Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (instancetype) connectionWithRegisteredName:(NSString *) name host:(NSString *) hostName;
```

## Parameters

- `name` — The name of an `NSConnection` object.

- `hostName` — The name of the host. The domain name `hostName` is an Internet domain name (for example, “`sales.anycorp.com`”). If `hostName` is `nil` or empty, then only the local host is searched for the named `NSConnection` object.

## Return Value

The `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under `name` on the host named `hostName`. Returns `nil` if no `NSConnection` object can be found for `name` and `hostName`. The returned `NSConnection` object is a child of the default `NSConnection` object for the current thread (that is, it shares the default `NSConnection` object’s receive port).

## Discussion

To get the object vended by the `NSConnection` object, use the [rootProxy](rootproxy.md) instance method. The [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) class method immediately returns this object.

## See Also

### Related Documentation

- [defaultConnection](defaultconnection.md) — Returns the default `NSConnection` object for the current thread. _(deprecated)_

### Getting a Remote Object

- [connectionWithRegisteredName:host:usingNameServer:](connectionwithregisteredname_host_usingnameserver_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host. _(deprecated)_
- [rootProxy](rootproxy.md) — The proxy for the root object of the receiver’s peer in another application or thread. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:](rootproxyforconnectionwithregisteredname_host_.md) — Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:usingNameServer:](rootproxyforconnectionwithregisteredname_host_usingnameserver_.md) — Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host. _(deprecated)_
- [remoteObjects](remoteobjects.md) — The local proxies for remote objects that have been received over the connection but not deallocated yet. _(deprecated)_
- [localObjects](localobjects.md) — The local objects that have been sent over the connection and still have proxies at the other end. _(deprecated)_
