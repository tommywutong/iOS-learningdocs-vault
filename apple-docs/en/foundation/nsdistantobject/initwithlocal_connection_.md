---
title: 'initWithLocal:connection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobject/initwithlocal:connection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobject/initwithlocal:connection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobject/initwithlocal%3Aconnection%3A.json'
content_hash: 'sha256:aa5a740167f52918'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObject](../nsdistantobject.md)

# initWithLocal:connection:

<sub>Instance Method</sub>

Initializes an `NSDistantObject` object as a local proxy for a given object.

<sub>Mac Catalyst, macOS</sub>

```objc
- (instancetype) initWithLocal:(id) target connection:(NSConnection *) connection;
```

## Parameters

- `target` — An object in the receiver’s address space.

- `connection` — The connection for the returned proxy.

## Return Value

An initialized `NSDistantObject` object that serves as a local proxy for `target`. If a proxy for `target` and `connection` already exists, the receiver is released and the existing proxy is retained and returned.

## Discussion

Other applications connect to the proxy using the `NSConnection` [connectionWithRegisteredName:host:](../nsconnection/connectionwithregisteredname_host_.md) class method.

Local proxies should be considered private to their `NSConnection` objects. Only an `NSConnection` object should use this method to create them, and your code shouldn’t retain or otherwise use local proxies.

This is the designated initializer for local proxies. It returns an initialized object, which might be different than the original receiver

## See Also

### Creating a Local Proxy

- [proxyWithLocal:connection:](proxywithlocal_connection_.md) — Returns a local proxy for a given object and connection, creating the proxy if necessary. _(deprecated)_
