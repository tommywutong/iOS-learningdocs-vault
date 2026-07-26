---
title: isEqual
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablecallbacks/isequal
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecallbacks/isequal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecallbacks/isequal.json'
content_hash: 'sha256:0c86478ae6c7d573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTableCallBacks](../nshashtablecallbacks.md)

# isEqual

<sub>Instance Property</sub>

Points to the function that compares second and third parameters. If `NULL`, then == is used for comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEqual: ((NSHashTable<AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?
```
