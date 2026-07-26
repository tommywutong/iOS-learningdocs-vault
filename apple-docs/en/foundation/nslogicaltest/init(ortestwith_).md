---
title: 'init(orTestWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslogicaltest/init(ortestwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslogicaltest/init(ortestwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslogicaltest/init%28ortestwith%3A%29.json'
content_hash: 'sha256:de90d92ed8bc507a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLogicalTest](../nslogicaltest.md)

# init(orTestWith:)

<sub>Initializer</sub>

Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.

<sub>Mac Catalyst, macOS</sub>

```swift
init(orTestWith subTests: [NSSpecifierTest])
```

## Parameters

- `subTests` — An array of `NSSpecifierTest` objects representing Boolean expressions.

## Return Value

An `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in `subTests`.

## See Also

### Initializing a logical test

- [- initAndTestWithTests:](<init(andtestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [- initNotTestWithTest:](<init(nottestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
