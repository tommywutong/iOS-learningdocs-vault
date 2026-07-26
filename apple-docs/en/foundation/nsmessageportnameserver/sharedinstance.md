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
doc_path: /documentation/foundation/nsmessageportnameserver/sharedinstance
source_url: 'https://developer.apple.com/documentation/foundation/nsmessageportnameserver/sharedinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmessageportnameserver/sharedinstance.json'
content_hash: 'sha256:d48d978fadb41956'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMessagePortNameServer](../nsmessageportnameserver.md)

# sharedInstance

<sub>Type Method</sub>

Returns the singleton instance of `NSMessagePortNameServer`.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) sharedInstance;
```

## Return Value

The singleton instance of `NSMessagePortNameServer` with which you register and look up `NSMessagePort` objects.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
