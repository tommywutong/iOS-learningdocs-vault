---
title: isMainThread
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/ismainthread-swift.type.property
source_url: 'https://developer.apple.com/documentation/foundation/thread/ismainthread-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/ismainthread-swift.type.property.json'
content_hash: 'sha256:5f99433b091b49cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isMainThread

<sub>Type Property</sub>

Returns a Boolean value that indicates whether the current thread is the main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var isMainThread: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the current thread is the main thread, otherwise [false](../../swift/false.md).

## See Also

### Working with the Main Thread

- [isMainThread](ismainthread-swift.property.md) — A Boolean value that indicates whether the receiver is the main thread.
- [mainThread](main.md) — Returns the `NSThread` object representing the main thread.
