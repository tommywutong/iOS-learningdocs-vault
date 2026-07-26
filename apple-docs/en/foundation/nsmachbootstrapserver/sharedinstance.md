---
title: sharedInstance
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmachbootstrapserver/sharedinstance
source_url: 'https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/sharedinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachbootstrapserver/sharedinstance.json'
content_hash: 'sha256:8ad98edb90959cbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachBootstrapServer](../nsmachbootstrapserver.md)

# sharedInstance

<sub>Type Method</sub>

Returns the shared instance of the bootstrap server.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) sharedInstance;
```

## Return Value

The shared instance of `NSMachBootstrapServer` with which you register and look up `NSMachPort` objects.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
