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
doc_path: /documentation/foundation/nsmaptablekeycallbacks/isequal
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/isequal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablekeycallbacks/isequal.json'
content_hash: 'sha256:0ea8192987fb89a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableKeyCallBacks](../nsmaptablekeycallbacks.md)

# isEqual

<sub>Instance Property</sub>

Points to the function which compares second and third parameters. If `NULL`, then == is used for comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEqual: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?
```
