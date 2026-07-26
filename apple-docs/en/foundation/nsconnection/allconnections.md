---
title: allConnections
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/allconnections
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/allconnections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/allconnections.json'
content_hash: 'sha256:ae0bfff28eeac624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# allConnections

<sub>Type Method</sub>

Returns all valid `NSConnection` objects in the process.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSArray<NSConnection *> *) allConnections;
```

## Return Value

An array containing all valid `NSConnection` objects in the process.

## See Also

### Related Documentation

- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
