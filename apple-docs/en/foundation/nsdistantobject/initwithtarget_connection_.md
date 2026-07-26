---
title: 'initWithTarget:connection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobject/initwithtarget:connection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobject/initwithtarget:connection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobject/initwithtarget%3Aconnection%3A.json'
content_hash: 'sha256:4b77e1a4ef3467da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObject](../nsdistantobject.md)

# initWithTarget:connection:

<sub>Instance Method</sub>

Initializes a newly allocated NSDistantObject as a remote proxy for `target`, which is an id in another thread or another application’s address space.

<sub>Mac Catalyst, macOS</sub>

```objc
- (instancetype) initWithTarget:(id) target connection:(NSConnection *) connection;
```

## Parameters

- `target` — An object in another thread or another application’s address space.

- `connection` — The connection to set as the `NSConnection` object for the returned proxy—it should have been created using the [connectionWithRegisteredName:host:](../nsconnection/connectionwithregisteredname_host_.md) class method.

## Return Value

An `NSDistantObject` object initialized as a remote proxy for `target`. If a proxy for `target` and `connection` already exists, the receiver is released and the existing proxy is retained and returned.

## Discussion

A remote proxy can’t be used until its connection’s peer has a local proxy representing `target` in the other application.

This is the designated initializer for remote proxies. It returns an initialized object, which might be different than the original receiver.

## See Also

### Creating a Remote Proxy

- [proxyWithTarget:connection:](proxywithtarget_connection_.md) — Returns a remote proxy for a given object and connection, creating the proxy if necessary. _(deprecated)_
