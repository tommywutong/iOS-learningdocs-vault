---
title: defaultConnection
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/defaultconnection
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/defaultconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/defaultconnection.json'
content_hash: 'sha256:d6f19ccb2f2edee7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# defaultConnection

<sub>Type Method</sub>

Returns the default `NSConnection` object for the current thread.

> [!warning] Deprecated
> Create individual connection instances as needed instead.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSConnection *) defaultConnection;
```

## Return Value

The default `NSConnection` object for the current thread, creating it if necessary.

## Discussion

The default `NSConnection` object uses a single `NSPort` object for both receiving and sending and is useful only for vending an object; use the [rootObject](rootobject-c.property.md) and [registerName:](registername_.md) methods to do this.

### Special Considerations

The singleton method of `NSConnection` has been deprecated. It was difficult to ensure that the shared connection wasn’t being used by other operations on the thread on which the default connection was requested. Using `[NSConnection new]` ensures that you get a unique connection object, preventing such collisions.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
