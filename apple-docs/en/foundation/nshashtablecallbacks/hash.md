---
title: hash
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablecallbacks/hash
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecallbacks/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecallbacks/hash.json'
content_hash: 'sha256:a95cef2d2607d902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTableCallBacks](../nshashtablecallbacks.md)

# hash

<sub>Instance Property</sub>

Points to the function that must produce hash code for elements of the hash table. If `NULL`, the pointer value is used as the hash code. Second parameter is the element for which hash code should be produced.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Int)?
```
