---
title: describe
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptablevaluecallbacks/describe
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks/describe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablevaluecallbacks/describe.json'
content_hash: 'sha256:f881511f3484d82d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTableValueCallBacks](../nsmaptablevaluecallbacks.md)

# describe

<sub>Instance Property</sub>

Points to the function that produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?
```
