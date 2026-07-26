---
title: retain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablecallbacks/retain
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecallbacks/retain.json'
content_hash: 'sha256:49c63c7baebb56a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTableCallBacks](../nshashtablecallbacks.md)

# retain

<sub>Instance Property</sub>

Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Void)?
```
