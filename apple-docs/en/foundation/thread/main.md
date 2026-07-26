---
title: main
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/main
source_url: 'https://developer.apple.com/documentation/foundation/thread/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/main.json'
content_hash: 'sha256:705034b3b47bcda0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# main

<sub>Type Property</sub>

Returns the `NSThread` object representing the main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var main: Thread { get }
```

## Return Value

The `NSThread` object representing the main thread.

## See Also

### Working with the Main Thread

- [isMainThread](ismainthread-swift.type.property.md) — Returns a Boolean value that indicates whether the current thread is the main thread.
- [isMainThread](ismainthread-swift.property.md) — A Boolean value that indicates whether the receiver is the main thread.
