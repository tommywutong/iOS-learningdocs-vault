---
title: child
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/child
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/child'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/child.json'
content_hash: 'sha256:6828502e86317db2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# child

<sub>Instance Property</sub>

Sets the receiver’s child reference.

<sub>Mac Catalyst, macOS</sub>

```swift
unowned(unsafe) var child: NSScriptObjectSpecifier? { get set }
```

## Parameters

- `child` — The receiver’s child reference.

## Discussion

Do not invoke this method directly; it is automatically invoked by [containerSpecifier](container.md).
