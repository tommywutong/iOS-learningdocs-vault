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
doc_path: /documentation/foundation/nsmaptablevaluecallbacks/retain
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablevaluecallbacks/retain.json'
content_hash: 'sha256:b20d594a5426589e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableValueCallBacks](../nsmaptablevaluecallbacks.md)

# retain

<sub>Instance Property</sub>

Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?
```
