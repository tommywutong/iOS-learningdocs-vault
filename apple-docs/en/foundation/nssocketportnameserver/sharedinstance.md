---
title: sharedInstance
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nssocketportnameserver/sharedinstance
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/sharedinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/sharedinstance.json'
content_hash: 'sha256:39910fa48ebedd47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# sharedInstance

<sub>Type Method</sub>

Returns the shared socket port name server.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
+ (id) sharedInstance;
```

## Return Value

The single instance of `NSSocketPortNameServer` with which you register and look up `NSSocketPort` objects.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
