---
title: 'proxyWithLocal:connection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobject/proxywithlocal:connection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobject/proxywithlocal:connection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobject/proxywithlocal%3Aconnection%3A.json'
content_hash: 'sha256:514f714efe3aa8d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObject](../nsdistantobject.md)

# proxyWithLocal:connection:

<sub>Type Method</sub>

Returns a local proxy for a given object and connection, creating the proxy if necessary.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) proxyWithLocal:(id) target connection:(NSConnection *) connection;
```

## Parameters

- `target` — An object in the receiver’s address space.

- `connection` — The connection for the returned proxy.

## Return Value

A local proxy for `target` and `connection`, creating it if necessary.

## Discussion

Other applications connect to the proxy using the `NSConnection` [connectionWithRegisteredName:host:](../nsconnection/connectionwithregisteredname_host_.md) class method.

Local proxies should be considered private to their `NSConnection` objects. Only an `NSConnection` object should use this method to create them, and your code shouldn’t retain or otherwise use local proxies.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Creating a Local Proxy

- [initWithLocal:connection:](initwithlocal_connection_.md) — Initializes an `NSDistantObject` object as a local proxy for a given object. _(deprecated)_
