---
title: release
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptablevaluecallbacks/release
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablevaluecallbacks/release.json'
content_hash: 'sha256:4b2b02a12f500127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableValueCallBacks](../nsmaptablevaluecallbacks.md)

# release

<sub>Instance Property</sub>

Points to the function that decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?
```
