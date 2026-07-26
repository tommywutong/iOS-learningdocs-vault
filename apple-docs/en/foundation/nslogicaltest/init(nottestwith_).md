---
title: 'init(notTestWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslogicaltest/init(nottestwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslogicaltest/init(nottestwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslogicaltest/init%28nottestwith%3A%29.json'
content_hash: 'sha256:a7293290de7149e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLogicalTest](../nslogicaltest.md)

# init(notTestWith:)

<sub>Initializer</sub>

Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.

<sub>Mac Catalyst, macOS</sub>

```swift
init(notTestWith subTest: NSScriptWhoseTest)
```

## Parameters

- `subTest` — The `NSScriptWhoseTest` object to invert.

## Return Value

An `NSLogicalTest` object initialized to perform a `NOT` operation on `subTest`.

## See Also

### Initializing a logical test

- [- initAndTestWithTests:](<init(andtestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [- initOrTestWithTests:](<init(ortestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.
