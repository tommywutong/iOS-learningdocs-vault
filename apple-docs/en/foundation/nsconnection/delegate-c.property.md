---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/delegate-c.property
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/delegate-c.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/delegate-c.property.json'
content_hash: 'sha256:2f084d1c7835c80c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (assign, nullable) id<NSConnectionDelegate> delegate;
```

## Discussion

A connection’s delegate can process incoming messages itself instead of letting `NSConnection` object handle them. The delegate can also authenticate messages and accept, deny, or modify new connections.
