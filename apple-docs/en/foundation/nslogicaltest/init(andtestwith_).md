---
title: 'init(andTestWith:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslogicaltest/init(andtestwith:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslogicaltest/init(andtestwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslogicaltest/init%28andtestwith%3A%29.json'
content_hash: 'sha256:1fc1ca50faad0025'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLogicalTest](../nslogicaltest.md)

# init(andTestWith:)

<sub>Initializer</sub>

Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.

<sub>Mac Catalyst, macOS</sub>

```swift
init(andTestWith subTests: [NSSpecifierTest])
```

## Parameters

- `subTests` — An array of `NSSpecifierTest` objects representing Boolean expressions.

## Return Value

An `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in `subTests`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Initializing a logical test

- [- initNotTestWithTest:](<init(nottestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
- [- initOrTestWithTests:](<init(ortestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.
