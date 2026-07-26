---
title: isMainThread
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/ismainthread-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/thread/ismainthread-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/ismainthread-swift.property.json'
content_hash: 'sha256:f855122c9d1a8d74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isMainThread

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is the main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isMainThread: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver is the main thread, otherwise [false](../../swift/false.md).

## See Also

### Working with the Main Thread

- [isMainThread](ismainthread-swift.type.property.md) — Returns a Boolean value that indicates whether the current thread is the main thread.
- [mainThread](main.md) — Returns the `NSThread` object representing the main thread.
