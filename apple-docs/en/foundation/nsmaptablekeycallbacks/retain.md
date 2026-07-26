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
doc_path: /documentation/foundation/nsmaptablekeycallbacks/retain
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablekeycallbacks/retain.json'
content_hash: 'sha256:20b5b88bae1b6ad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableKeyCallBacks](../nsmaptablekeycallbacks.md)

# retain

<sub>Instance Property</sub>

Points to the function which increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?
```
