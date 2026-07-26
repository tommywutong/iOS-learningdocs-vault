---
title: 'proxyWithTarget:connection:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobject/proxywithtarget:connection:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobject/proxywithtarget:connection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobject/proxywithtarget%3Aconnection%3A.json'
content_hash: 'sha256:aa880f2b6b61ed3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObject](../nsdistantobject.md)

# proxyWithTarget:connection:

<sub>Type Method</sub>

Returns a remote proxy for a given object and connection, creating the proxy if necessary.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) proxyWithTarget:(id) target connection:(NSConnection *) connection;
```

## Parameters

- `target` — An object in another thread or another application’s address space.

- `connection` — The connection to set as the `NSConnection` object for the returned proxy—it should have been created using the `NSConnection` [connectionWithRegisteredName:host:](../nsconnection/connectionwithregisteredname_host_.md) class method.

## Return Value

A remote proxy for `target` and `connection`, creating the proxy if necessary

## Discussion

A remote proxy cannot be used until its connection’s peer has a local proxy representing `target` in the other application.

## See Also

### Creating a Remote Proxy

- [initWithTarget:connection:](initwithtarget_connection_.md) — Initializes a newly allocated NSDistantObject as a remote proxy for `target`, which is an id in another thread or another application’s address space. _(deprecated)_
